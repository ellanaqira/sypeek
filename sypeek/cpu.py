import subprocess


class CPUInfoError(Exception):
    """
    Exception raised and displays an error message
    when a problem occurs while trying to retrieve
    cpu information.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def _return_cpu_error(keyword_error: str):
    # raised CPUInfoError
    raise CPUInfoError(f"Couldn't get cpu '{keyword_error}' information")


def _get_data(command:str, keyword:str, keyword_error: str):
    try:
        data = subprocess.run(command, capture_output=True, text=True)

    except FileNotFoundError:
        _return_cpu_error(keyword_error)
    
    else:
        data = data.stdout.splitlines()
        for line in data:
            if keyword in line:
                try:
                    return line.split(':')[1].strip()
                except IndexError:
                    return line.split('=')[1].strip()
                
        return _return_cpu_error(keyword_error)
         
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

    get_vendor_id = _get_data("lscpu", "Vendor ID", "Vendor")
    vendor = vendor_id_dict.get(get_vendor_id)
    
    # handling vendor id not found
    if vendor == None:
        return f"vendor name of '{get_vendor_id}' could not be found"
    else:
        return vendor
    

def cpu_vendorid():
    return _get_data("lscpu", "Vendor ID", "Vendor ID")

def cpu_name():
    # return cpu model name
    return _get_data("lscpu", "Model name", "Model Name")

def cpu_threads():
    # return number of thread(s) per core
    return int(_get_data("lscpu", "Thread", "Thread"))   


def cpu_cores(core: str):
    _CPU_CORES_ERROR_MESSAGE = "core must be 'l' or 'p'"

    try:
        # return number of cpu logical core(s)
        if core.lower() == 'l':
            return int(_get_data("lscpu", "Core(s) per socket", "Logical Core")) * int(_get_data("lscpu", "Thread", "Logical Core"))
            
        # return number of cpu physical core(s)
        elif core.lower() == 'p':
            return int(_get_data("lscpu", "Core(s) per socket", "Physical Core"))
        
        else:
            return _CPU_CORES_ERROR_MESSAGE
        
    except AttributeError:
        return _CPU_CORES_ERROR_MESSAGE


def cpu_family():
    # return cpu family
    return _get_data("cpuid", "family", "Family")

def cpu_family_synth():
    # return cpu family synth
    return _get_data("cpuid", "family synth", "Family Synth")

def cpu_model():
    # return cpu model
    return _get_data("cpuid", "model", "Model")
    
def cpu_model_synth():
    # return cpu model synth
    return _get_data("cpuid", "model synth", "Model Synth")

def cpu_stepping():
    # return cpu stepping value
    return int(_get_data("lscpu", "Stepping", "Stepping"))

       
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
        return _return_cpu_error("Speed")

    else:
        _CPU_SPEED_ERROR_MESSAGE = f"core number must be int() and between 0 and {len(cpus)-1}"

        if type(core_num) != int:
            return _CPU_SPEED_ERROR_MESSAGE
        
        else:
            if core_num < 0 or core_num >= len(cpus):
                return _CPU_SPEED_ERROR_MESSAGE
        
            if cpus[core_num].get("cppu MHz"):
                return float(cpus[core_num].get("cpu MHz"))
            else:
                _return_cpu_error("Speed")
 

def cpu_temp(scale: str):
    celcius = float(_get_data("sensors", "Tctl", "Temperature").replace('+','').replace("°C",''))
    
    _CPU_TEMPERATURE_ERROR_MESSAGE = "temperature scale must be 'c', 'f', or 'k'"

    try:
        if scale.lower() == 'c':
            return celcius # Celcius
        elif scale.lower() == 'f':
            return (celcius * 9/5) + 32 # Fahrenheit
        elif scale.lower() == 'k':
            return celcius + 273.15 # Kelvin
        else:
            return _CPU_TEMPERATURE_ERROR_MESSAGE
    
    except AttributeError:
        return _CPU_TEMPERATURE_ERROR_MESSAGE
     

def _get_level_cache(order: int, keyword_error: str):
    # get cache level data from cpuid
    try:
        cpuid_data = subprocess.run("cpuid", capture_output=True, text=True)

    except FileNotFoundError:
        _return_cpu_error(keyword_error)
    
    else:
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
        try:    
            return int(cpuid_new_list[order])
        except IndexError:
            return _return_cpu_error(keyword_error)


def cpu_l1c(cache_type: str):
    _CPU_LEVEL1_CACHE_ERROR_MESSAGE = "cache type must be 'd' or 'i'"

    try:
        if cache_type.lower() == 'd': # Level 1 data cache
            return _get_level_cache(0, "Data Cache Level 1 ")
        elif cache_type.lower() == 'i': # Level 1 instruction cache
            return _get_level_cache(1, "Instruction Cache Level 1 ")
        else:
            return _CPU_LEVEL1_CACHE_ERROR_MESSAGE
        
    except AttributeError:
        return _CPU_LEVEL1_CACHE_ERROR_MESSAGE


def cpu_l2c():
    # return cpu Level 2 cache
    return _get_level_cache(2, "Cache Level 2")

def cpu_l3c():
    # return cpu Level 3 cache
    return _get_level_cache(3, "Cache Level 3")
