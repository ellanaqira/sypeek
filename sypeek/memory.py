import subprocess

def total():
    # return total memory
    result = subprocess.run("free", capture_output=True, text=True).stdout
    result = result.split('\n')
    for k in result:
        if "Mem" in k:
            k = float(k.split()[1].strip()) / 1000000
            return f"{k:.2f}"

def used():
    # return used memory
    result = subprocess.run("free", capture_output=True, text=True).stdout
    result = result.split('\n')
    for k in result:
        if "Mem" in k:
            k = float(k.split()[2].strip()) / 1000000
            return f"{k:.2f}"  
        
def available():
    # return available memory
    result = subprocess.run("free", capture_output=True, text=True).stdout
    result = result.split('\n')
    for k in result:
        if "Mem" in k:
            k =  float(k.split()[6].strip()) / 1000000
            return f"{k:.2f}"

def free():
    # return free memory
    result = subprocess.run("free", capture_output=True, text=True).stdout
    result = result.split('\n')
    for k in result:
        if "Mem" in k:
            k = float(k.split()[3].strip()) / 1000000
            return f"{k:.2f}"

            