import subprocess


def _get_data(about: str, keyword: str):
    data_list = []
    data_dict = {}

    try:
        data = subprocess.run("free", capture_output=True, text=True)
    except FileNotFoundError:
        return "something went wrong, couldn't get data from memory"
    else:
        data = data.stdout.splitlines()
        for line in data:
            line = line.split()
            data_list.append(line)

        if about == "memo":
            del data_list[1][0], data_list[2]
        elif about == "swap":
            del data_list[1], data_list[1][0]

        for key, value in zip(data_list[0], data_list[1]):
            data_dict[key] = value

        # return value in kibibytes - 1 kibibyte (KiB) is 1024 bytes.    
        return int(data_dict[keyword])
    


# Memory ==============================================

def mem_total():
    # return total memory
    return _get_data("memo", "total")

def mem_used():
    # return used memory
    return _get_data("memo", "used")

def mem_free():
    # return free memory
    return _get_data("memo", "free")

def mem_available():
    # return available memory
    return _get_data("memo", "available")


# Swap Memory =========================================

def swap_mem_total():
    # return total swap memory
    return _get_data("swap", "total")

def swap_mem_used():
    # return used swap memory
    return _get_data("swap", "used")

def swap_mem_free():
    # return free swap memory
    return _get_data("swap", "free")
            