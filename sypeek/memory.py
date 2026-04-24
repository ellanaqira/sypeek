import subprocess

def total():
    # return total memory in Gigabytes
    result = subprocess.run("free | grep 'Mem'", shell=True ,capture_output=True, text=True).stdout
    result = float(result.split()[1].strip()) / 1000000
    return result

def used():
    # return used memory in Gigabytes
    result = subprocess.run("free | grep 'Mem'", shell=True, capture_output=True, text=True).stdout
    result = float(result.split()[2].strip()) / 1000000
    return result
        
def free():
    # return free memory
    result = subprocess.run("free | grep 'Mem'", shell=True, capture_output=True, text=True).stdout
    result = float(result.split()[3].strip()) / 1000000
    return result

def available():
    # return available memory
    result = subprocess.run("free | grep 'Mem'", shell=True, capture_output=True, text=True).stdout
    result = float(result.split()[6].strip()) / 1000000
    return result
            