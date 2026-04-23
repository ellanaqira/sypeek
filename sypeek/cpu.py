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

def family_synth():
    # return cpu family synth
    fam_syn = subprocess.run("cpuid | grep -m1 'family synth'", shell=True, capture_output=True, text=True).stdout
    return fam_syn.split('=')[1].strip()

def model():
    # return cpu model
    modl = subprocess.run("cpuid | grep -m1 'model'", shell=True, capture_output=True, text=True).stdout
    return modl.split('=')[1].strip()

def model_synth():
    # return cpu model synth
    modl_syn = subprocess.run("cpuid | grep -m1 'model synth'", shell=True, capture_output=True, text=True).stdout
    return modl_syn.split('=')[1].strip()

def stepping():
    # return cpu stepping value
    step = subprocess.run("lscpu | grep -m1 'Stepping'", shell=True, capture_output=True, text=True).stdout
    return int(step.split(':')[1].strip())
       
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
    cputemp = subprocess.run("sensors | grep -m1 'Tctl'", shell=True, capture_output=True, text=True).stdout
    return float(cputemp.split(":")[1].strip().replace('+','').replace("°C",''))

def L1d(sum=False):
    # return Level 1 data cache
    if sum == False:
        l1d_sum = subprocess.run("lscpu | grep 'L1d'", shell=True, capture_output=True, text=True).stdout
        l1d_sum = l1d_sum.split(':')[1].strip().split()
        l1d = int(l1d_sum[0].strip()) # get Level 1 data cache value that already multyplied by instances
        ins = int(l1d_sum[2].strip().replace('(','')) # get number of instances
        return int(l1d / ins) # devide L1 data cache with number of instances to return L1 data cacahe for single instances
    elif sum == True:
        l1d_sum = subprocess.run("lscpu | grep 'L1d'", shell=True, capture_output=True, text=True).stdout
        l1d_sum = l1d_sum.split(':')[1].strip()
        return l1d_sum
