import subprocess 

def vendorid():
    # return processor vendors id name
    cpu_venid = subprocess.run("lscpu | grep 'Vendor ID'", shell=True, capture_output=True, text=True).stdout
    return cpu_venid.split(':')[1].strip()
         
def vendor():
    # return processor vendors name
    id_ext = ["Authentic", "CPU", "Driven", "Geode by NSC", "Genuine", "isbetter!", "RiseRise", "Sis Sis", "UMC UMC", "VIA VIA"] # processor manufacturer ID string
    cpu_ven = subprocess.run("lscpu | grep 'Vendor ID'", shell=True, capture_output=True, text=True).stdout
    cpu_ven = cpu_ven.split(':')[1].strip()
    for ext in id_ext:
        if ext in cpu_ven:
            return cpu_ven.replace(ext, '')

def name():
    # return cpu model name
    model_name = subprocess.run("lscpu | grep 'Model name'", shell=True, capture_output=True, text=True).stdout
    return model_name.split(':')[1].strip()          
            
def cores():
    # return number of cpu cores
    core = subprocess.run("lscpu | grep 'Core'", shell=True, capture_output=True, text=True).stdout
    return int(core.split(':')[1].strip())

def threads():
    # return number of threads
    thread = subprocess.run("lscpu | grep 'Thread'", shell=True, capture_output=True, text=True).stdout
    thread = int(thread.split(':')[1].strip())
    return thread * cores()

def family():
    # return cpu family
    fam = subprocess.run("cpuid | grep -m1 'family'", shell=True, capture_output=True, text=True).stdout
    return fam.split('=')[1].strip()
print(family())
def family_synth():
    # return cpu family synth
    result = subprocess.run("cpuid", capture_output=True, text=True).stdout
    result = result.split('\n')
    for k in result:
        if "(family synth)" in k:
            k = k.split('=')[1].strip()
            return k
            
def model_synth():
    # return cpu model synth
    result = subprocess.run("cpuid", capture_output=True, text=True).stdout
    result = result.split('\n')
    for k in result:
        if "(model synth)" in k:
            k = k.split('=')[1].strip()
            return k

def model():
    # return cpu model
    result = subprocess.run("cpuid", capture_output=True, text=True).stdout
    result = result.split('\n')
    for k in result:
        if "model" in k:
            k = k.split('=')[1].strip()
            return k

def stepping():
    # return cpu stepping value
    with open('/proc/cpuinfo', 'r') as file:
        for line in file:
            if line.startswith('stepping'):
                return(line.split(':')[1].strip())
            
def speed(threads_num):
    # thread_num for number of threads
    # get threads speed in MHz by the number
    if threads_num < 0 or threads_num > (threads()-1):
        return f"not included: thread number ({threads_num}) does not match the number of threads, which is (0-{threads()-1})"
    else:
        with open('/proc/cpuinfo', 'r') as file:
            for line in file:
                if line.startswith(f"processor	: {threads_num}"):
                    for line in file:
                        if line.startswith("cpu MHz"):
                            return(line.split(':')[1].strip())          

def temp():
    # return cpu temperature in celcius
    result = subprocess.run("sensors", capture_output=True, text=True).stdout
    result = result.split('\n')
    for k in result:
        if "Tctl" in k:
            k = k.split(':')[1].strip()
            return float(k.replace('+','').replace("°C",''))
