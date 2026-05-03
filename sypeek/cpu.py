import subprocess
from pathlib import Path

def _get_data(command:str, keyword:str):
    try:
        data = subprocess.run(command, capture_output=True, text=True)
    except FileNotFoundError:
        return "something went wrong, couldn't get data from cpu"
    else:
        data = data.stdout.splitlines()
        for line in data:
            if keyword in line:
                try:
                    return line.split(':')[1].strip()
                except IndexError:
                    return line.split('=')[1].strip()
                
        return "something went wrong, couldn't get data from cpu"
         
def cpu_vendor():
    vendor_id_dict = {
        # general vendor id
        "AuthenticAMD": "AMD",
        "CentaurHauls": "IDT",
        "CyrixInstead": "Cyrix",
        "GenuineIntel": "Intel",
        "GenuineIotel": "Intel",
        "TransmetaCPU": "Transmeta",
        "GenuineTMx86": "Transmeta",
        "Geode by NSC": "National Semiconductor",
        "NexGenDriven": "NexGen",
        "RiseRiseRise": "Rise",
        "SiS SiS SiS ": "SiS",
        "UMC UMC UMC ": "UMC",
        "Vortex86 SoC": "DM&P",
        "  Shanghai  ": "Zhaoxin",
        "HygonGenuine": "Hygon",
        "Genuine  RDC": "RDC Semiconductor",
        "E2K MACHINE ": "MCST",
        "VIA VIA VIA ": "VIA",
        "AMD ISBETTER": "AMD",

        # open source CPU cores
        "GenuineAo486": "ao486",
        "MiSTer AO486": "ao486",

        # virtual machines / emulator
        "ConnectixCPU": "Connectix",
        "Virtual CPU ": "Microsoft",
        "Insignia 586": "Insignia",
        "Compaq FX!32": "Compaq",
        "PowerVM Lx86": "IBM",
        "Neko Project": "Neko Project",
    }

    get_vendor_id = _get_data("lscpu", "Vendor ID")
    vendor = vendor_id_dict.get(get_vendor_id)
    
    # handling vendor id not found
    if vendor == None:
        return f"vendor name of cpu could not be found"
    else:
        return vendor
    

def cpu_vendorid():
    return _get_data("lscpu", "Vendor ID")
    
def cpu_name():
    # return cpu model name
    return _get_data("lscpu", "Model name")
 

def cpu_threads():
    # return number of thread(s) per core
    try:
        return int(_get_data("lscpu", "Thread"))
    except ValueError:
        return _get_data("lscpu", "Thread")
    

def cpu_cores(core: str):
    try:
        # return number of cpu logical core(s)
        if core.lower() == 'l':
            try:
                return int(_get_data("lscpu", "Core(s) per socket")) * int(_get_data("lscpu", "Thread"))
            except:
                return _get_data("lscpu", "Core(s) per socket")
            
        # return number of cpu physical core(s)
        elif core.lower() == 'p':
            try:
                return int(_get_data("lscpu", "Core(s) per socket"))
            except ValueError:
                return _get_data("lscpu", "Core(s) per socket")
        
        else:
            return "core must be 'l' or 'p'"
        
    except AttributeError:
        return "core must be 'l' or 'p'"


def cpu_family():
    # return cpu family
    return _get_data("cpuid", "family")

def cpu_family_synth():
    # return cpu family synth
    return _get_data("cpuid", "family synth")

def cpu_model():
    # return cpu model
    return _get_data("cpuid", "model")
    
def cpu_model_synth():
    # return cpu model synth
    return _get_data("cpuid", "model synth")

def cpu_stepping():
    # return cpu stepping value
    try:
        return int(_get_data("lscpu", "Stepping"))
    except ValueError:
        return _get_data("lscpu", "Stepping")

       
def cpu_speed(core_num: int):
    # return core speed in MHz by the number of order (core_num)
    cpus = []
    try:
        with open("/proc/cpuinfo") as f:
            cpu = {}
            for line in f:
                line = line.strip()

                if not line:
                    if cpu:
                        cpus.append(cpu)
                        cpu = {}
                    continue
                key, value = [x.strip() for x in line.split(":", 1)]
                cpu[key] = value
            # store the last cpu information, because there is no empty line at the end of the file  
            if cpu:
                cpus.append(cpu)

    except FileNotFoundError:
        return "something went wrong, couldn't get data from cpu"

    else:
        if type(core_num) != int:
            return f"core number must be int() and between 0 and {len(cpus)-1}"
        
        else:
            if core_num < 0 or core_num >= len(cpus):
                return f"core number must be int() and between 0 and {len(cpus)-1}"
        
            return float(cpus[core_num].get("cpu MHz", 0))
 

def cpu_temp(scale: str):
    try:
        celcius = float(_get_data("sensors", "Tctl").replace('+','').replace("°C",''))

    except ValueError: 
        return _get_data("sensors", "Tctl")
    
    else:
        try:
            if scale.lower() == 'c':
                return celcius # Celcius
            elif scale.lower() == 'f':
                return (celcius * 9/5) + 32 # Fahrenheit
            elif scale.lower() == 'k':
                return celcius + 273.15 # Kelvin
            else:
                return "temperature scale must be 'c', 'f', or 'k'"
        
        except AttributeError:
            return "temperature scale must be 'c', 'f', or 'k'"
                    

def _get_level_cache(order: int):
    # get cache level data from cpuid
    cpuid_data = subprocess.run("cpuid", capture_output=True, text=True)
    cpuid_data = cpuid_data.stdout.splitlines()
    cpuid_list = []
    for line in cpuid_data:
        line = line.strip()
        if line.startswith("(synth size)"):
            line = line.split('=')[1].strip()
            cpuid_list.append(line)
            continue

    cpuid_list = list(dict.fromkeys(cpuid_list))

    cpuid_new_list = []
    for element in cpuid_list:
        element = element.split()[0].strip()
        cpuid_new_list.append(int(element))
        
    # return value in kibibytes - 1 kibibyte (KiB) is 1024 bytes.    
    return int(cpuid_new_list[order])


def cpu_l1c(cache_type: str):
    try:
        if cache_type.lower() == 'd': # Level 1 data cache
            return _get_level_cache(0)
        elif cache_type.lower() == 'i': # Level 1 instruction cache
            return _get_level_cache(1)
        else:
            return ("cache type must be 'd' or 'i'")
        
    except AttributeError:
        return "cache type must be 'd' or 'i'"


def cpu_l2c():
    # return cpu Level 2 cache
    return _get_level_cache(2)

def cpu_l3c():
    # return cpu Level 3 cache
    return _get_level_cache(3)
