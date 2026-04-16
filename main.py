def vendor():
    # return processor vendor name
    with open('/proc/cpuinfo', 'r') as file:
        for line in file:
            if line.startswith('vendor'):
                return(line.split(":")[1].strip())

def proc_name():
    # return processor model name
    with open('/proc/cpuinfo', 'r') as file:
        for line in file:
            if line.startswith('model name'):
                return(line.split(":")[1].strip())
            
def cpu_family():
    # return processor model name
    with open('/proc/cpuinfo', 'r') as file:
        for line in file:
            if line.startswith('cpu family'):
                return(line.split(":")[1].strip())
            
def cpu_model():
    # return processor model name
    with open('/proc/cpuinfo', 'r') as file:
        for line in file:
            if line.startswith('model'):
                return(line.split(":")[1].strip())
            