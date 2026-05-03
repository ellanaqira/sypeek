import subprocess


_MEMO_GENERAL_ERROR_MESSAGE = "something went wrong, couldn't get data from memory"


def _get_data(about: str, keyword: str):
    data_list = []
    data_dict = {}

    try:
        data = subprocess.run("free", capture_output=True, text=True)

    except FileNotFoundError:
        return _MEMO_GENERAL_ERROR_MESSAGE
    
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

        try:
            # return value in kibibytes - 1 kibibyte (KiB) is 1024 bytes.    
            return int(data_dict[keyword])
        
        except ValueError:
            return _MEMO_GENERAL_ERROR_MESSAGE
        
        except KeyError:
            return _MEMO_GENERAL_ERROR_MESSAGE
   


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
            