class MemoInfoError(Exception):
    """
    Exception raised and displays an error message
    when a problem occurs while trying to retrieve
    memory information.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


def _return_memo_error(keyword_error: str):
    # raised MemoInfoError
    raise MemoInfoError(f"Couldn't get '{keyword_error}' information")


def _get_memo_data_meminfo(keyword: str, keyword_error: str):
    data_dict = {}
    try:
        with open("/proc/meminfo") as f:
            for line in f:
                key, value = [x.strip().replace("kB", '').replace("kb", '') for x in line.split(':', 1)]
                data_dict[key] = value.strip()
                
    except FileNotFoundError:
        _return_memo_error(keyword_error)
    
    else:
        # return value in bytes
        try:
            return int(data_dict[keyword])
        except KeyError:
            _return_memo_error(keyword_error)



# General Memory ===============================================

def mem_total():
    # return total memory
    return _get_memo_data_meminfo("MemTotal", "Total Memory")

def mem_free():
    # return free memory
    return _get_memo_data_meminfo("MemFree", "Free Memory")

def mem_avlbl():
    # return available memory
    return _get_memo_data_meminfo("MemAvailable", "Available Memory")

def mem_used():
    # return used memory
    try:
        total_mem = _get_memo_data_meminfo("MemTotal", None)
        avail_mem = _get_memo_data_meminfo("MemAvailable", None)
    except MemoInfoError:
        raise _return_memo_error("Used Memory")
    else:
        return total_mem - avail_mem



# Active Memory ================================================

def mem_act():
    # return active memory recently
    return _get_memo_data_meminfo("Active", "Active Memory")

def mem_inact():
    # return inactive memory
    return _get_memo_data_meminfo("Inactive", "Inactive Memory")


def mem_actanon():
    # return active memory (anon)
    return _get_memo_data_meminfo("Active(anon)", "Active Memory (anon)")


def mem_inactanon():
    # return active memory (anon)
    return _get_memo_data_meminfo("Inactive(anon)", "Inactive Memory (anon)")


def mem_actfile():
    """
    The (file) means that the amount
    of memory is being used by cache.
    """
    # return active memory (file)
    return _get_memo_data_meminfo("Active(file)", "Active Memory (file)")


def mem_inactfile():
    # return inactive memory (file)
    return _get_memo_data_meminfo("Inactive(file)", "Inactive Memory (file)")



# Buffers and Cache ============================================

def mem_buffer():
    """
    Buffer is a part of memory which stores data temporarily
    while that data is being forwarded from one location to
    another in a computer. 
    """
    # return memory buffer
    return _get_memo_data_meminfo("Buffers", "Memory Buffer")


def mem_cache():
    # return memory cache
    return _get_memo_data_meminfo("Cached", "Memory Cache")



# Swap Memory ==================================================

def mem_swptotal():
    # return the total amount of swap space available in the system
    return _get_memo_data_meminfo("SwapTotal", "Total Swap Space")

def mem_swpfree():
    # return the value of unused swap space
    return _get_memo_data_meminfo("SwapFree", "Free Swap Space")

def mem_swpcache():
    # return the value of recently used swap memory
    return _get_memo_data_meminfo("SwapCached", "Swap Cache")



# Writeback into the Disk ======================================

def mem_wrbk():
    # return value of memory that is being written back at the moment
    return _get_memo_data_meminfo("Writeback", "Memory Write Back")


def mem_dirty():
    # return value of memory that is currently waiting to be written back to disk after being modified (dirty).
    return _get_memo_data_meminfo("Dirty", "Dirty Memory")



# Shared Memory ================================================

def mem_shr():
    # return the amount used by shared memory and the tmpfs filesystem
    return _get_memo_data_meminfo("Shmem", "Shared Memory")


def mem_shrhp():
    # return the amount used by shared memory and the tmpfs filesystem with huge pages
    return _get_memo_data_meminfo("ShmemHugePages", "Shared Memory (Huge Pages)")



# Kernel Memory ================================================

def mem_krec():
    # return the value of kernel allocated memory, reclaimable under memory pressure
    return _get_memo_data_meminfo("KReclaimable", "Reclaimable Memory")

def mem_slab():
    # return total memory used by kernel slab caches
    return _get_memo_data_meminfo("Slab", "Memory Slab")

def mem_srec():
    # return the amount of slab memory part that can be reclaimed under memory pressure
    return _get_memo_data_meminfo("SReclaimable", "Reclaimable Memory Slab")

def mem_sunrec():
    # return the amount of slab memory part that cannot be reclaimed, even when the system is low on memory
    return _get_memo_data_meminfo("SUnreclaim", "Unclaimable Memory Slab")

def mem_kstack():
    # return the sum of all kernel stack memory
    return _get_memo_data_meminfo("KernelStack", "Kernel Stack Memory")
