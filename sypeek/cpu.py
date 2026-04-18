import subprocess 

def vendorid():
    # return processor vendors id name
    with open('/proc/cpuinfo', 'r') as file:
        for line in file:
            if line.startswith('vendor_id'):
                return(line.split(":")[1].strip())
            
def vendor():
    # return processor vendors name
    # processor manufacturer ID string
    id_ext = ["Authentic", "CPU", "Driven", "Geode by NSC", "Genuine", "isbetter!", "RiseRise", "Sis Sis", "UMC UMC", "VIA VIA"]
    with open('/proc/cpuinfo', 'r') as file:
        for line in file:
            if line.startswith('vendor_id'):
                line = line.split(':')[1].strip()
                for i in id_ext:
                    if i in line:
                        line = line.replace(i,'')
                    else:
                        line
                return line 

def name():
    # return processor name
    with open('/proc/cpuinfo', 'r') as file:
        for line in file:
            if line.startswith('model name'):
                return (line.split(":")[1].strip())
            
def cores():
    # return number of cpu cores
    with open('/proc/cpuinfo', 'r') as file:
        for line in file:
            if line.startswith('cpu cores'):
                return int(line.split(':')[1].strip())
   
def threads():
    # return number of threads
    thread_num = 0
    with open('/proc/cpuinfo', 'r') as file:
        for line in file:
            if line.startswith('processor'):
                thread_num += 1
    return(thread_num)

def family():
    # return cpu family
    result = subprocess.run("cpuid", capture_output=True, text=True).stdout
    result = result.split('\n')
    for k in result:
        if "family" in k:
            k = k.split('=')[1].strip()
            return k
    
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
