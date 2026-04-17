def vendor():
    # return processor vendor name
    with open('/proc/cpuinfo', 'r') as file:
        for line in file:
            if line.startswith('vendor_id'):
                return(line.split(":")[1].strip())

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
