import subprocess


class MemoInfoError(Exception):
    """
    Exception raised and displays an error message
    when a problem occurs while trying to retrieve
    memory information.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
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
                data_dict[key] = value
                
    except FileNotFoundError:
        _return_memo_error(keyword_error)
    
    else:
        """
        1 KiB = 1024 bytes
        1 KB  = 1000 bytes

        based on the information above
        1 KiB = (1024 / 1000) KB
        1 KiB = 1.024 KB
        """
        # return value in Kilobytes
        return int(data_dict[keyword]) * 1.024



def _get_memo_data_free(keyword: str, keyword_error: str):
    mem_data_list = []
    mem_data_dict = {}

    try:
        mem_datas = subprocess.run("free", capture_output=True, text=True)
    except FileNotFoundError:
        _return_memo_error(keyword_error)

    else:
        mem_datas = mem_datas.stdout.split('\n')

        for mem_data in mem_datas:
            mem_data_list.append(mem_data.split())
        
        del mem_data_list[1][0], mem_data_list[2]

        for key, value in zip(mem_data_list[0], mem_data_list[1]):
            mem_data_dict[key] = value
        
        # return value in Kilobytes
        return int(mem_data_dict[keyword]) * 1.024
    

    
class _Return_Data:
    def __init__(self, keyword: str, keyword_error: str):
        self.keyword = keyword
        self.keyword_error = keyword_error
    
    def _show_meminfo_memo_data(self):
        try:
            return _get_memo_data_meminfo(self.keyword, self.keyword_error)
        except KeyError:
            _return_memo_error(self.keyword_error)

    def _show_free_memo_data(self):
        try:
            return _get_memo_data_free(self.keyword, self.keyword_error)
        except KeyError:
            _return_memo_error(self.keyword_error)



# General Memory ===============================================

def mem_total():
    # return total memory
    total_memo = _Return_Data("MemTotal", "Total Memory")
    return total_memo._show_meminfo_memo_data()

def mem_free():
    # return free memory
    free_memo = _Return_Data("MemFree", "Free Memory")
    return free_memo._show_meminfo_memo_data()

def mem_available():
    # return available memory
    available_memo = _Return_Data("MemAvailable", "Available Memory")
    return available_memo._show_meminfo_memo_data()

def mem_used():
    # return used memory
    used_memo = _Return_Data("used", "Used Memorys")
    return used_memo._show_free_memo_data()



# Active Memory ================================================

def mem_active():
    # return active memory recently
    active_memo = _Return_Data("Active", "Active Memory")
    return active_memo._show_meminfo_memo_data()

def mem_inactive():
    # return inactive memory
    incative_memo = _Return_Data("Inactive", "Inactive Memory")
    return incative_memo._show_meminfo_memo_data()


def mem_active_anon():
    """
    The (anon) means that this amount of memory
    is being used by a service or application.
    """
    # return active memory (anon)
    active_memo_anon = _Return_Data("Active(anon)", "Active Memory (anon)")
    return active_memo_anon._show_meminfo_memo_data()

def mem_inactive_anon():
    # return active memory (anon)
    inactive_memo_anon = _Return_Data("Inactive(anon)", "Inactive Memory (anon)")
    return inactive_memo_anon._show_meminfo_memo_data()


def mem_active_file():
    """
    The (file) means that the amount
    of memory is being used by cache.
    """
    # return active memory (file)
    active_memo_file = _Return_Data("Active(file)", "Active Memory (file)")
    return active_memo_file._show_meminfo_memo_data()

def mem_inactive_file():
    # return inactive memory (file)
    inactive_memo_file = _Return_Data("Inactive(file)", "Inactive Memory (file)")
    return inactive_memo_file._show_meminfo_memo_data()



# Buffers and Cache ============================================

def mem_buffer():
    """
    Buffer is a part of memory which stores data temporarily
    while that data is being forwarded from one location to
    another in a computer. 
    """
    # return memory buffer
    memo_buffer = _Return_Data("Buffers", "Memory Buffer")
    return memo_buffer._show_meminfo_memo_data()


def mem_cache():
    """
    Cache is a fast storage unit that is not too large in size
    compared to other memory units and is used to store data
    that has been accessed recently.
    """
    # return memory cache
    memo_cache = _Return_Data("Cached", "Memory Cache")
    return memo_cache._show_meminfo_memo_data()



# Swap Memory ==================================================

def mem_swap_total():
    # return the total amount of swap space available in the system
    swap_memo_total = _Return_Data("SwapTotal", "Total Swap Space")
    return swap_memo_total._show_meminfo_memo_data()

def mem_swap_free():
    # return the value of unused swap space
    swap_memo_free = _Return_Data("SwapFree", "Free Swap Space'")
    return swap_memo_free._show_meminfo_memo_data()

def mem_swap_cache():
    # return the value of recently used swap memory
    swap_memo_cache = _Return_Data("SwapCached", "Swap Cache")
    return swap_memo_cache._show_meminfo_memo_data()



# Writeback into the Disk ======================================

def mem_writesback():
    """
    Write back is when the data is updated only in the cache and
    updated into the memory at a later time. Data is updated in
    the memory only when the cache line is ready to be replaced. 
    """
    # return value of memory that is being written back at the moment
    writeback_memo = _Return_Data("Writeback", "Memory Write Back")
    return writeback_memo._show_meminfo_memo_data()

def mem_dirty():
    # return value of memory that is currently waiting to be written back to disk after being modified (dirty).
    dirty_bit_memo = _Return_Data("Dirty", "Dirty Memory")
    return dirty_bit_memo._show_meminfo_memo_data()



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
    shared_memo = _Return_Data("Shmem", "Shared Memory")
    return shared_memo._show_meminfo_memo_data()

def mem_shared_hp():
    # return the amount used by shared memory and the tmpfs filesystem with huge pages
    shared_memo_huge_pages = _Return_Data("ShmemHugePages", "Shared Memory (Huge Pages)")
    return shared_memo_huge_pages._show_meminfo_memo_data()



# Kernel Memory ================================================

def mem_kreclaimable():
    """
    Kernel allocations that the kernel will attempt to reclaim
    under memory pressure. Includes other direct allocations
    with a shrinker
    """
    # return the value of kernel allocated memory, reclaimable under memory pressure
    kernel_reclaimable_memo = _Return_Data("KReclaimable", "Reclaimable Memory")
    return kernel_reclaimable_memo._show_meminfo_memo_data()

def mem_slab():
    """
    A slab is a set of one or more contiguous pages of memory
    set aside by the slab allocator for an individual cache.
    This memory is further divided into equal segments the size
    of the object type that the cache is managing.
    """
    # return total memory used by kernel slab caches
    slab = _Return_Data("Slab", "Memory Slab")
    return slab._show_meminfo_memo_data()

def mem_sreclaimable():
    # return the amount of slab memory part that can be reclaimed under memory pressure
    slab_reclaimable = _Return_Data("SReclaimable", "Reclaimable Memory Slab")
    return slab_reclaimable._show_meminfo_memo_data()

def mem_sunreclaim():
    # return the amount of slab memory part that cannot be reclaimed, even when the system is low on memory
    slab_unreclaimable = _Return_Data("SUnreclaim", "Unclaimable Memory Slab")
    return slab_unreclaimable._show_meminfo_memo_data()

def mem_kernel_stack():
    # return the sum of all kernel stack memory
    kernel_stack = _Return_Data("KernelStack", "Kernel Stack Memory")
    return kernel_stack._show_meminfo_memo_data()
