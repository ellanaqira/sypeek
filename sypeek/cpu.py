import subprocess

def _get_data(command, keyword):
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

def cores(core = ''):
    # return number of cpu logical core(s)
    if core == 'l':
        return int(_get_data("lscpu", "Core(s) per socket")) * threads()
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
       
def speed(threads_num):
    # thread_num for number of threads
    # get threads speed in MHz by the number
    if threads_num < 0 or threads_num > (cores(core='l')-1):
        return f"not included: thread number ({threads_num}) does not match the number of threads, which is (0-{cores(core='l')-1})"
    else:
        with open('/proc/cpuinfo') as f:
            for line in f:
                if line.startswith(f"processor	: {threads_num}"):
                    for line in f:
                        if line.startswith("cpu MHz"):
                            return(line.split(':')[1].strip())  

def temp():
    # return cpu temperature in celcius
    return(_get_data("sensors", "Tctl").replace('+','').replace("°C",''))

# def L1(cache=''):
#     # return level 1 data cache
#     if cache == 'd':
#         l1 = subprocess.run("cpuid | grep -m4 'synth size'", shell=True, capture_output=True, text=True).stdout
#         l1 = int(l1.split('\n')[0].split()[3].strip())
#         return l1
#     # return level 1 data instruction
#     elif cache == 'i':
#         l1 = subprocess.run("cpuid | grep -m4 'synth size'", shell=True, capture_output=True, text=True).stdout
#         l1 = int(l1.split('\n')[1].split()[3].strip())
#         return l1
