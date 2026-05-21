import subprocess
import os

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



# _get_cpu_data_from_cpuinfo function ==============================================================

def _get_cpu_data_from_cpuinfo(keyword: str, keyword_error: str, core_num: int = 0):
    # function to retrive information from cpuinfo file
    cpu_list = []
    try:
        with open("/proc/cpuinfo") as f:
            cpu_dict = {}
            for line in f:
                line = line.strip()

                if not line:
                    if cpu_dict:
                        cpu_list.append(cpu_dict)
                        cpu_dict = {}
                    continue
                key, value = [x.strip() for x in line.split(":", 1)]
                cpu_dict[key] = value

            # store the last cpu information, because there is no empty line at the end of the file  
            if cpu_dict:
                cpu_list.append(cpu_dict)

    except FileNotFoundError:
        return _return_cpu_error(keyword_error)

    else:
        _CORE_NUM_ERROR_MESSAGE = f"core number must be int() and between 0 and {len(cpu_list)-1}"

        if type(core_num) != int:
            return _CORE_NUM_ERROR_MESSAGE

        elif core_num < 0 or core_num > (len(cpu_list)-1):
            return _CORE_NUM_ERROR_MESSAGE

        elif keyword == "all cores":
            return len(cpu_list)
        
        else:
            try:
                if cpu_list[core_num].get(keyword):
                    return float(cpu_list[core_num].get(keyword))
                
                else:
                    _return_cpu_error(keyword_error)
                
            except TypeError:
                _return_cpu_error(keyword_error)


# functions that rely on _get_cpu_data_from_cpuinfo function
def cpu_cores(core_type: str):
    _CPU_CORES_ERROR_MESSAGE = "core type must be 'l' or 'p'"

    try:
        # return number of cpu physical core(s)
        if core_type.lower() == 'p':
            return int(_get_cpu_data_from_cpuinfo("cpu cores", "Physical Core"))
        
        # return number of cpu logical core(s)
        elif core_type.lower() == 'l':
            return int(_get_cpu_data_from_cpuinfo("all cores", "Logical Core"))
        
        else:
            return _CPU_CORES_ERROR_MESSAGE
        
    except AttributeError:
        return _CPU_CORES_ERROR_MESSAGE

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

    get_vendor_id = _get_cpu_data_from_cpuinfo("vendor_id", "Vendor")
    vendor = vendor_id_dict.get(get_vendor_id)
    
    # handling vendor id not found
    if vendor == None:
        return f"vendor name of '{get_vendor_id}' could not be found"
    else:
        return vendor  

def cpu_vendorid():
    return _get_cpu_data_from_cpuinfo("vendor_id", "Vendor ID")

def cpu_model_name():
    # return cpu model name
    return _get_cpu_data_from_cpuinfo("model name", "Model Name")

def cpu_stepping():
    # return cpu stepping value
    return int(_get_cpu_data_from_cpuinfo("stepping", "Stepping"))

def cpu_speed(core_num: int):
    # return cpu speed
    return _get_cpu_data_from_cpuinfo("cpu MHz", "Speed", core_num)



# _get_cpu_data_from_command function ==============================================================

def _get_cpu_data_from_command(command:str, keyword:str, keyword_error: str):
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


# functions that rely on _get_cpu_data_from_command function
def cpu_threads():
    # return number of thread(s) per core
    return int(_get_cpu_data_from_command("lscpu", "Thread", "Thread"))   

def cpu_family():
    # return cpu family
    return _get_cpu_data_from_command("cpuid", "family", "Family")

def cpu_family_synth():
    # return cpu family synth
    return _get_cpu_data_from_command("cpuid", "family synth", "Family Synth")

def cpu_model():
    # return cpu model
    return _get_cpu_data_from_command("cpuid", "model", "Model")
    
def cpu_model_synth():
    # return cpu model synth
    return _get_cpu_data_from_command("cpuid", "model synth", "Model Synth")

def cpu_temp(scale: str):
    celcius = float(_get_cpu_data_from_command("sensors", "Tctl", "Temperature").replace('+','').replace("°C",''))
    
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
    


# _get_cpu_cache_level function ====================================================================

def _get_cpu_cache_info(num_of_index_folder: int, keyword: str):
    try:
        path_folder: str = f"/sys/devices/system/cpu/cpu0/cache/index{num_of_index_folder}"
        level_cache_dict = {}

        with os.scandir(path_folder) as folder:
            for file in folder:
                if file.is_file and file.name.endswith(""):
                    with open(file.path, encoding='utf-8') as f:
                        key = (f.name.split('/')[-1])
                        value = (f.read().strip())

                        level_cache_dict[key] = value

    except FileNotFoundError:
        _return_cpu_error("Cache Level")
    else:
        return level_cache_dict[keyword]
    

# functions that rely on _get_cpu_cache_info function
def cpu_l1c(cache_type: str):
    _CPU_LEVEL1_CACHE_ERROR_MESSAGE = "cache type must be 'd' or 'i'"

    try:
        if cache_type.lower() == 'd': # Level 1 data cache in byte
            try:
                d_cache_size = int((_get_cpu_cache_info(0, "size")).replace("K", ""))
                return d_cache_size * 1024
            except ValueError:
                return _get_cpu_cache_info(0, "size")

        
        elif cache_type.lower() == 'i': # Level 1 instruction cache in byte
            try:
                i_cache_size = int((_get_cpu_cache_info(1, "size")).replace("K", ""))
                return i_cache_size * 1024
            except ValueError:
                return _get_cpu_cache_info(1, "size")
    
        else:
            return _CPU_LEVEL1_CACHE_ERROR_MESSAGE
        
    except AttributeError:
        return _CPU_LEVEL1_CACHE_ERROR_MESSAGE


def cpu_l2c():
    # return cpu Level 2 cache in byte
    try:
        cache_size = int((_get_cpu_cache_info(2, "size")).replace("K", ""))
        return cache_size * 1024
    except ValueError:
        return _get_cpu_cache_info(2, "size")
        

def cpu_l3c():
    # return cpu Level 3 cache in byte
    try:
        cache_size = int((_get_cpu_cache_info(3, "size")).replace("K", ""))
        return cache_size * 1024
    except ValueError:
        return _get_cpu_cache_info(3, "size")
    