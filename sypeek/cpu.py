def vendorid():
    # return processor vendors id name
    with open('/proc/cpuinfo', 'r') as file:
        for line in file:
            if line.startswith('vendor_id'):
                return(line.split(":")[1].strip())
            
def vendor():
    # return processor vendors name
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
print(vendor())   

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
                return (line.split(':')[1].strip())
   
def threads():
    # return number of threads
    thread_num = 0
    with open('/proc/cpuinfo', 'r') as file:
        for line in file:
            if line.startswith('processor'):
                thread_num += 1
    return(thread_num)

def family():
    # return cpu family value
    with open('/proc/cpuinfo', 'r') as file:
        for line in file:
            if line.startswith('cpu family'):
                return (line.split(":")[1].strip())
            
def model():
    # return cpu model value
    with open('/proc/cpuinfo', 'r') as file:
        for line in file:
            if line.startswith('model'):
                return(line.split(":")[1].strip())
            
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