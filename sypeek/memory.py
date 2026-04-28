import subprocess

def _get_free_data(keyword:str, index:int):
    data = subprocess.run("free", capture_output=True, text=True)
    data = data.stdout.splitlines()
    for line in data:
        if keyword in line:
            return line.split()[index].strip()
    return None

def total():
    # return total memory in Gigabytes
    return float(_get_free_data("Mem", 1)) / 1000000

def used():
    # return used memory in Gigabytes
    return float(_get_free_data("Mem", 2)) / 1000000

def free():
    # return free memory in Gigabytes
    return float(_get_free_data("Mem", 3)) / 1000000

def available():
    # return available memory in Gigabytes
    return float(_get_free_data("Mem", 6)) / 1000000
            