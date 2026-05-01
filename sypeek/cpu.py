import subprocess

def _get_data(command:str, keyword:str):
    data = subprocess.run(command, capture_output=True, text=True)
    data = data.stdout.splitlines()
    for line in data:
        if keyword in line:
            try:
                return line.split(':')[1].strip()
            except IndexError:
                return line.split('=')[1].strip()
    return None
         
def vendor():
    id_ext = {
        "AuthenticAMD" : "AMD",
        "GenuineIntel" : "Intel",
        "TransmetaCPU" : "Transmeta",
        "GenuineTMx86" : "Transmeta",
        "NexGenDriven" : "NexGen",
        "RiseRiseRise" : "Rise",
        "SiS SiS SiS " : "SiS",
        "UMC UMC UMC " : "UMC",
        "HygonGenuine" : "Hygon",
        "CentaurHauls" : "VIA"
    }
    vendor_id = _get_data("lscpu", "Vendor ID")
    return id_ext.get(vendor_id)


def vendorid():
    return _get_data("lscpu", "Vendor ID")
    
def name():
    # return cpu model name
    return _get_data("lscpu", "Model name")   

def threads():
    # return number of thread(s) per core
    return int(_get_data("lscpu", "Thread"))

def cores(core: str):
    if type(core) != str:
        raise ValueError("core must be 'l' or 'p'")
    
    else:
        # return number of cpu logical core(s)
        if core.lower() == 'l':
            return int(_get_data("lscpu", "Core(s) per socket")) * int(_get_data("lscpu", "Thread"))
        # return number of cpu physical core(s)
        elif core.lower() == 'p':
            return int(_get_data("lscpu", "Core(s) per socket"))
        
        else:
            raise ValueError("core must be 'l' or 'p'")

def family():
    # return cpu family
    return _get_data("cpuid", "family")

def family_synth():
    # return cpu family synth
    return _get_data("cpuid", "family synth")

def model():
    # return cpu model
    return _get_data("cpuid", "model")
    
def model_synth():
    # return cpu model synth
    return _get_data("cpuid", "model synth")

def stepping():
    # return cpu stepping value
    return int(_get_data("lscpu", "Stepping"))

       
def speed(core_num: int):
    # return core speed in MHz by the number of order (core_num)
    cpus = []
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

    if type(core_num) != int:
        raise ValueError(f"core number must be between 0 and {len(cpus)-1}")
    
    else:
        if core_num < 0 or core_num >= len(cpus):
            raise ValueError(f"core number must be between 0 and {len(cpus)-1}")
        
        return float(cpus[core_num].get("cpu MHz", 0))


def temp(scale: str):
    if type(scale) != str:
        raise ValueError(f"temperature scale must be 'c', 'f', or 'k'")
    
    else:
        celcius = float(_get_data("sensors", "Tctl").replace('+','').replace("°C",''))
        if scale.lower() == 'c':
            return celcius # Celcius
        elif scale.lower() == 'f':
            return (celcius * 9/5) + 32 # Fahrenheit
        elif scale.lower() == 'k':
            return celcius + 273.15 # Kelvin
            
        else:
            raise ValueError(f"temperature scale must be 'c', 'f', or 'k'")
        

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


def l1(cache_type: str):
    if type(cache_type) != str:
        raise ValueError("cache type must be 'd' or 'i'")
    
    else:
        if cache_type.lower() == 'd': # Level 1 data cache
            return _get_level_cache(0)
        elif cache_type.lower() == 'i': # Level 1 instruction cache
            return _get_level_cache(1)
        else:
            raise ValueError("cache type must be 'd' or 'i'")

def l2():
    # return cpu Level 2 cache
    return _get_level_cache(2)

def l3():
    # return cpu Level 3 cache
    return _get_level_cache(3)
