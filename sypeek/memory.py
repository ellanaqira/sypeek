import subprocess

def _get_free_data(keyword: str):
    memory = []
    memo_data = {}
    data = subprocess.run("free", capture_output=True, text=True)
    data = data.stdout.splitlines()
    for line in data:
        line = line.split()
        memory.append(line)
        continue

    del memory[1][0], memory[2]

    for key, value in zip(memory[0], memory[1]):
        memo_data[key] = value
        continue

    # return value in kibibytes - 1 kibibyte (KiB) is 1024 bytes.    
    return int(memo_data[keyword])

def total():
    # return total memory
    return _get_free_data("total")

def used():
    # return used memory
    return _get_free_data("used")

def free():
    # return free memory
    return _get_free_data("free")

def available():
    # return available memory
    return _get_free_data("available")

            