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

def vendorid():
    # return processor vendors id name
    return _get_data("lscpu", "Vendor ID")
         
def vendor():
    # return processor vendors name
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
    
def name():
    # return cpu model name
    return _get_data("lscpu", "Model name")   

def threads():
    # return number of thread(s) per core
    return int(_get_data("lscpu", "Thread"))

def cores(core: str):
    # return number of cpu logical core(s)
    if core == 'l':
        return int(_get_data("lscpu", "Core(s) per socket")) * int(_get_data("lscpu", "Thread"))
    # return number of cpu physical core(s)
    elif core == 'f':
        return int(_get_data("lscpu", "Core(s) per socket"))

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
                # if reach the empty line
                if cpu:
                    cpus.append(cpu)
                    cpu = {}
                continue
            # split the line by ':' and added the key and value into cpu dictionary
            key, value = [x.strip() for x in line.split(":", 1)]
            cpu[key] = value
        # store the last cpu info, because there is no empty line at the end of the file  
        if cpu:
            cpus.append(cpu)
    # return ValueError if core_num is out of range
    if core_num < 0 or core_num >= len(cpus):
        raise ValueError(f"core number must be between 0 and {len(cpus)-1}")
     # return core speed
    return float(cpus[core_num].get("cpu MHz", 0))

def temp(scale: str):
    # get cpu temperature in Celcius
    celcius = float(_get_data("sensors", "Tctl").replace('+','').replace("°C",''))
    # return cpu temperature in Celcius
    if scale == 'c':
        return celcius
    # return cpu temperature in Fahrenheit 
    elif scale == 'f':
        return (celcius * 9/5) + 32
    # return cpu temperature in Kelvin
    elif scale == 'k':
        return celcius + 273.15
    else:
        raise ValueError(f"'{scale}' is not included.")
