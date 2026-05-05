
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


def mem_active_anon():
    """
    The (anon) means that this amount of memory
    is being used by a service or application.
    """
    # return active memory (anon)
    active_memo_anon = _Return_Data("Active(anon)")
    return active_memo_anon._get_memo_data()

def mem_inactive_anon():
    # return active memory (anon)
    inactive_memo_anon = _Return_Data("Inactive(anon)")
    return inactive_memo_anon._get_memo_data()


def mem_active_file():
    """
    The (file) means that the amount
    of memory is being used by cache.
    """
    # return active memory (file)
    active_memo_file = _Return_Data("Active(file)")
    return active_memo_file._get_memo_data()

def mem_inactive_file():
    # return inactive memory (file)
    inactive_memo_file = _Return_Data("Inactive(file)")
    return inactive_memo_file._get_memo_data()



# Buffers and Cache ============================================

def mem_buffer():
    """
    Buffer is a part of memory which stores data temporarily
    while that data is being forwarded from one location to
    another in a computer. 
    """
    # return memory buffer
    memo_buffer = _Return_Data("Buffers")
    return memo_buffer._get_memo_data()


def mem_cache():
    """
    Cache is a fast storage unit that is not too large in size
    compared to other memory units and is used to store data
    that has been accessed recently.
    """
    # return memory cache
    memo_cache = _Return_Data("Cached")
    return memo_cache._get_memo_data()



# Swap Memory ==================================================

def mem_swap_total():
    # return the total amount of swap space available in the system
    swap_memo_total = _Return_Data("SwapTotal")
    return swap_memo_total._get_memo_data()

def mem_swap_free():
    # return the value of unused swap space
    swap_memo_free = _Return_Data("SwapFree")
    return swap_memo_free._get_memo_data()

def mem_swap_cache():
    # return the value of recently used swap memory
    swap_memo_cache = _Return_Data("SwapCached")
    return swap_memo_cache._get_memo_data()



# Writeback into the Disk ======================================

def mem_writesback():
    """
    Write back is when the data is updated only in the cache and
    updated into the memory at a later time. Data is updated in
    the memory only when the cache line is ready to be replaced. 
    """
    # return value of memory that is being written back at the moment
    writeback_memo = _Return_Data("Writeback")
    return writeback_memo._get_memo_data()

def mem_dirty():
    # return value of memory that is currently waiting to be written back to disk after being modified (dirty).
    dirty_bit_memo = _Return_Data("Dirty")
    return dirty_bit_memo._get_memo_data()



# Shared Memory ================================================

def mem_shared():
    """
    Tmpfs (temporary file system) tmpfs is a file system
    which keeps all files in virtual memory. Everything
    in tmpfs is temporary in the sense that no files will
    be created on your hard drive. If you unmount a tmpfs
    instance, everything stored therein is lost.
    """
    # return the amount used by shared memory and the tmpfs filesystem
    shared_memo = _Return_Data("Shmem")
    return shared_memo._get_memo_data()

def mem_shared_hp():
    # return the amount used by shared memory and the tmpfs filesystem with huge pages
    shared_memo_huge_pages = _Return_Data("ShmemHugePages")
    return shared_memo_huge_pages._get_memo_data()
