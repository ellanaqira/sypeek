
_GENERAL_MEMO_ERROR_MESSAGE = "Sorry, something went wrong, couldn't get data from memory"

def _get_memo_datas(keyword: str):
    data_dict = {}
    try:
        with open("/proc/meminfo") as f:
            for line in f:
                key, value = [x.strip().replace("kB", '').replace("kb", '') for x in line.split(':', 1)]
                data_dict[key] = value
                
    except FileNotFoundError:
        return _GENERAL_MEMO_ERROR_MESSAGE
    
    else:
        # return value in Kilobyte
        return int(data_dict[keyword])
   

class _Return_Data:
    def __init__(self, keyword: str):
        self.keyword = keyword
    
    def _get_memo_data(self):
        try:
            return _get_memo_datas(self.keyword)
        except KeyError:
            return _GENERAL_MEMO_ERROR_MESSAGE


# General Memory ===============================================

def mem_total():
    # return total memory
    total_memo = _Return_Data("MemTotal")
    return total_memo._get_memo_data()

def mem_free():
    # return free memory
    free_memo = _Return_Data("MemFree")
    return free_memo._get_memo_data()

def mem_available():
    # return available memory
    available_memo = _Return_Data("MemAvailable")
    return available_memo._get_memo_data()



# Active Memory ================================================

def mem_active():
    # return active memory recently
    active_memo = _Return_Data("Active")
    return active_memo._get_memo_data()

def mem_inactive():
    # return inactive memory
    incative_memo = _Return_Data("Inactive")
    return incative_memo._get_memo_data()

"""
The (anon) means that this amount of memory
is being used by a service or application.
"""

def mem_active_anon():
    # return active memory (anon)
    active_memo_anon = _Return_Data("Active(anon)")
    return active_memo_anon._get_memo_data()

def mem_inactive_anon():
    # return active memory (anon)
    inactive_memo_anon = _Return_Data("Inactive(anon)")
    return inactive_memo_anon._get_memo_data()

"""
The (file) means that the amount
of memory is being used by cache.
"""

def mem_active_file():
    # return active memory (file)
    active_memo_file = _Return_Data("Active(file)")
    return active_memo_file._get_memo_data()

def mem_inactive_file():
    # return inactive memory (file)
    inactive_memo_file = _Return_Data("Inactive(file)")
    return inactive_memo_file._get_memo_data()
