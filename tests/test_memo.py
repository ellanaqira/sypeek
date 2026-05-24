import pytest
from unittest.mock import patch

from sypeek import memory


class _Return_Notfile_Exception_Memo:
    def __init__ (self, keyword: str, keyword_error: str):
        self.keyword = keyword
        self.keyword_error = keyword_error
        self.exception_msg: str = f"Couldn't get '{self.keyword_error}' information"

    # simulate if the meminfo file doesn't exist so it returns an exception
    def _notfile_meminfo_exception(self):
        with patch("sypeek.memory._get_memo_data_meminfo", side_effect=memory.MemoInfoError(self.exception_msg)):
            with pytest.raises(memory.MemoInfoError) as excinfo:
                memory._get_memo_data_meminfo(self.keyword, self.keyword_error)
            assert excinfo.value.message == self.exception_msg



class _Return_Keyword_Exception_Memo:
    def __init__(self, keyword_error: str):
        self.keyword_error = keyword_error
        self.exception_msg: str = f"Couldn't get '{self.keyword_error}' information"

    # simulate if the keyword from meminfo file doesn't exist so it returns an exception
    def _meminfo_keyword_exeption(self):
        with pytest.raises(memory.MemoInfoError) as excinfo:
            memory._get_memo_data_meminfo("invalid_keyword", self.keyword_error)
        assert excinfo.value.message == self.exception_msg



class _Mock_Function:
    # mock the return value
    def __init__(self):
        self.mocked_value: float = 1999999.999

    def _mock_meminfo_func(self, mocker_plugin):
        mock_meminfo_func = mocker_plugin.patch("sypeek.memory._get_memo_data_meminfo")
        mock_meminfo_func.return_value = self.mocked_value



# General Memory ===============================================

# total memory
def test_mock_mem_total(mocker):
    _Mock_Function()._mock_meminfo_func(mocker)
    assert memory.mem_total() == _Mock_Function().mocked_value

def test_notfile_exception_mem_total():
    _Return_Notfile_Exception_Memo("MemTotal", "Total Memory")._notfile_meminfo_exception()

def test_keyword_exception_mem_total():
    _Return_Keyword_Exception_Memo("Total Memory")._meminfo_keyword_exeption()


# free memory
def test_mock_mem_free(mocker):
    _Mock_Function()._mock_meminfo_func(mocker)
    assert memory.mem_free() == _Mock_Function().mocked_value

def test_notfile_exception_mem_free():
    _Return_Notfile_Exception_Memo("MemFree", "Free Memory")._notfile_meminfo_exception()

def test_keyword_exception_mem_free():
    _Return_Keyword_Exception_Memo("Free Memory")._meminfo_keyword_exeption()


# available memory
def test_mock_mem_available(mocker):
    _Mock_Function()._mock_meminfo_func(mocker)
    assert memory.mem_free() == _Mock_Function().mocked_value

def test_notfile_exception_mem_available():
    _Return_Notfile_Exception_Memo("MemAvailable", "Available Memory")._notfile_meminfo_exception()

def test_keyword_exception_mem_available():
    _Return_Keyword_Exception_Memo("Available Memory")._meminfo_keyword_exeption()


# used memory
def test_mock_mem_used(mocker):
    mocked_value: float = 1999999.999
    mock_meminfo_func = mocker.patch("sypeek.memory.mem_used")
    mock_meminfo_func.return_value = mocked_value
    assert memory.mem_used() == mocked_value

def test_notfile_exception_mem_used():
    _Return_Notfile_Exception_Memo("used", "Used Memory")._notfile_meminfo_exception()

def test_keyword_exception_mem_used():
    _Return_Keyword_Exception_Memo("Used Memory")._meminfo_keyword_exeption()



# Active Memory ================================================

# active memory
def test_mock_mem_active(mocker):
    _Mock_Function()._mock_meminfo_func(mocker)
    assert memory.mem_active() == _Mock_Function().mocked_value

def test_notfile_exception_mem_active():
    _Return_Notfile_Exception_Memo("Active", "Active Memory")._notfile_meminfo_exception()

def test_keyword_exception_mem_active():
    _Return_Keyword_Exception_Memo("Active Memory")._meminfo_keyword_exeption()


# inactive memory
def test_mock_mem_inactive(mocker):
    _Mock_Function()._mock_meminfo_func(mocker)
    assert memory.mem_inactive() == _Mock_Function().mocked_value

def test_notfile_exception_mem_inactive():
    _Return_Notfile_Exception_Memo("Inactive", "Inactive Memory")._notfile_meminfo_exception()

def test_keyword_exception_mem_inactive():
    _Return_Keyword_Exception_Memo("Inactive Memory")._meminfo_keyword_exeption()


# active memory (anon)
def test_mock_mem_active_anon(mocker):
    _Mock_Function()._mock_meminfo_func(mocker)
    assert memory.mem_active_anon() == _Mock_Function().mocked_value

def test_notfile_exception_mem_active_anon():
    _Return_Notfile_Exception_Memo("Active(anon)", "Active Memory (anon)")._notfile_meminfo_exception()

def test_keyword_exception_mem_active_anon():
    _Return_Keyword_Exception_Memo("Active Memory (anon)")._meminfo_keyword_exeption()


# inactive memory (anon)
def test_mock_mem_inactive_anon(mocker):
    _Mock_Function()._mock_meminfo_func(mocker)
    assert memory.mem_inactive_anon() == _Mock_Function().mocked_value

def test_notfile_exception_mem_inactive_anon():
    _Return_Notfile_Exception_Memo("Inactive(anon)", "Inactive Memory (anon)")._notfile_meminfo_exception()

def test_keyword_exception_mem_inactive_anon():
    _Return_Keyword_Exception_Memo("Inactive Memory (anon)")._meminfo_keyword_exeption()


# active memory (file)
def test_mock_mem_active_file(mocker):
    _Mock_Function()._mock_meminfo_func(mocker)
    assert memory.mem_active_file() == _Mock_Function().mocked_value

def test_notfile_exception_mem_active_file():
    _Return_Notfile_Exception_Memo("Active(file)", "Active Memory (file)")._notfile_meminfo_exception()

def test_keyword_exception_mem_active_file():
    _Return_Keyword_Exception_Memo("Active Memory (file)")._meminfo_keyword_exeption()


# inactive memory (file)
def test_mock_mem_inactive_file(mocker):
    _Mock_Function()._mock_meminfo_func(mocker)
    assert memory.mem_inactive_file() == _Mock_Function().mocked_value

def test_notfile_exception_mem_inactive_file():
    _Return_Notfile_Exception_Memo("Inactive(file)", "Inactive Memory (file)")._notfile_meminfo_exception()

def test_keyword_exception_mem_inactive_file():
    _Return_Keyword_Exception_Memo("Inactive Memory (file)")._meminfo_keyword_exeption()



# Buffers and Cache ============================================

# memory buffer
def test_mock_mem_buffer(mocker):
    _Mock_Function()._mock_meminfo_func(mocker)
    assert memory.mem_buffer() == _Mock_Function().mocked_value

def test_notfile_exception_mem_buffer():
    _Return_Notfile_Exception_Memo("Buffers", "Memory Buffer")._notfile_meminfo_exception()

def test_keyword_exception_mem_buffer():
    _Return_Keyword_Exception_Memo("Memory Buffer")._meminfo_keyword_exeption()


# memory cache
def test_mock_mem_cache(mocker):
    _Mock_Function()._mock_meminfo_func(mocker)
    assert memory.mem_cache() == _Mock_Function().mocked_value

def test_notfile_exception_mem_cache():
    _Return_Notfile_Exception_Memo("Cached", "Memory Cache")._notfile_meminfo_exception()

def test_keyword_exception_mem_cache():
    _Return_Keyword_Exception_Memo("Memory Cache")._meminfo_keyword_exeption()



# Swap Memory ==================================================

# memory swap total
def test_mock_mem_swap_total(mocker):
    _Mock_Function()._mock_meminfo_func(mocker)
    assert memory.mem_swap_total() == _Mock_Function().mocked_value

def test_notfile_exception_mem_swap_total():
    _Return_Notfile_Exception_Memo("SwapTotal", "Total Swap Space")._notfile_meminfo_exception()

def test_keyword_exception_mem_swap_total():
    _Return_Keyword_Exception_Memo("Total Swap Space")._meminfo_keyword_exeption()


# unused/free swap memory
def test_mock_mem_swap_free(mocker):
    _Mock_Function()._mock_meminfo_func(mocker)
    assert memory.mem_swap_free() == _Mock_Function().mocked_value

def test_notfile_exception_mem_swap_free():
    _Return_Notfile_Exception_Memo("SwapFree", "Free Swap Space")._notfile_meminfo_exception()

def test_keyword_exception_mem_swap_free():
    _Return_Keyword_Exception_Memo("Free Swap Space")._meminfo_keyword_exeption()


# memory swap cache
def test_mock_mem_swap_cache(mocker):
    _Mock_Function()._mock_meminfo_func(mocker)
    assert memory.mem_swap_cache() == _Mock_Function().mocked_value

def test_notfile_exception_mem_swap_cache():
    _Return_Notfile_Exception_Memo("SwapCached", "Swap Cache")._notfile_meminfo_exception()

def test_keyword_exception_mem_swap_cache():
    _Return_Keyword_Exception_Memo("Swap Cache")._meminfo_keyword_exeption()



# Writeback into the Disk ======================================

# memory writesback
def test_mock_mem_writesback(mocker):
    _Mock_Function()._mock_meminfo_func(mocker)
    assert memory.mem_writesback() == _Mock_Function().mocked_value

def test_notfile_exception_mem_writesback():
    _Return_Notfile_Exception_Memo("Writeback", "Memory Write Back")._notfile_meminfo_exception()

def test_keyword_exception_mem_writesback():
    _Return_Keyword_Exception_Memo("Memory Write Back")._meminfo_keyword_exeption()


# memory dirty
def test_mock_mem_dirty(mocker):
    _Mock_Function()._mock_meminfo_func(mocker)
    assert memory.mem_dirty() == _Mock_Function().mocked_value

def test_notfile_exception_mem_dirty():
    _Return_Notfile_Exception_Memo("Dirty", "Dirty Memory")._notfile_meminfo_exception()

def test_keyword_exception_mem_dirty():
    _Return_Keyword_Exception_Memo("Dirty Memory")._meminfo_keyword_exeption()



# Shared Memory ================================================

# shared memory
def test_mock_mem_shared(mocker):
    _Mock_Function()._mock_meminfo_func(mocker)
    assert memory.mem_shared() == _Mock_Function().mocked_value

def test_notfile_exception_mem_shared():
    _Return_Notfile_Exception_Memo("Shmem", "Shared Memory")._notfile_meminfo_exception()

def test_keyword_exception_mem_shared():
    _Return_Keyword_Exception_Memo("Shared Memory")._meminfo_keyword_exeption()


# shared memory (huge pages)
def test_mock_mem_shared_huge_pages(mocker):
    _Mock_Function()._mock_meminfo_func(mocker)
    assert memory.mem_shared_hp() == _Mock_Function().mocked_value

def test_notfile_exception_mem_shared_huge_pages():
    _Return_Notfile_Exception_Memo("ShmemHugePages", "Shared Memory (Huge Pages)")._notfile_meminfo_exception()

def test_keyword_exception_mem_shared_huge_pages():
    _Return_Keyword_Exception_Memo("Shared Memory (Huge Pages)")._meminfo_keyword_exeption()



# Kernel Memory ================================================

# kernel reclaimable memory
def test_mock_mem_kernel_reclaimable(mocker):
    _Mock_Function()._mock_meminfo_func(mocker)
    assert memory.mem_kreclaimable() == _Mock_Function().mocked_value

def test_notfile_exception_mem_kernel_reclaimable():
    _Return_Notfile_Exception_Memo("KReclaimable", "Reclaimable Memory")._notfile_meminfo_exception()

def test_keyword_exception_mem_kernel_reclaimable():
    _Return_Keyword_Exception_Memo("Reclaimable Memory")._meminfo_keyword_exeption()


# kernel slab memory
def test_mock_mem_kernel_slab(mocker):
    _Mock_Function()._mock_meminfo_func(mocker)
    assert memory.mem_slab() == _Mock_Function().mocked_value

def test_notfile_exception_mem_kernel_slab():
    _Return_Notfile_Exception_Memo("Slab", "Memory Slab")._notfile_meminfo_exception()

def test_keyword_exception_mem_kernel_slab():
    _Return_Keyword_Exception_Memo("Memory Slab")._meminfo_keyword_exeption()


# kernel slab memory (reclaimable)
def test_mock_mem_kernel_slab_reclaimable(mocker):
    _Mock_Function()._mock_meminfo_func(mocker)
    assert memory.mem_sreclaimable() == _Mock_Function().mocked_value

def test_notfile_exception_mem_kernel_slab_reclaimable():
    _Return_Notfile_Exception_Memo("SReclaimable", "Reclaimable Memory Slab")._notfile_meminfo_exception()

def test_keyword_exception_mem_kernel_slab_reclaimable():
    _Return_Keyword_Exception_Memo("Reclaimable Memory Slab")._meminfo_keyword_exeption()


# kernel slab memory (unclaimable)
def test_mock_mem_kernel_slab_unreclaimable(mocker):
    _Mock_Function()._mock_meminfo_func(mocker)
    assert memory.mem_sunreclaim() == _Mock_Function().mocked_value

def test_notfile_exception_mem_kernel_slab_unreclaimable():
    _Return_Notfile_Exception_Memo("SUnreclaim", "Unclaimable Memory Slab")._notfile_meminfo_exception()

def test_keyword_exception_mem_kernel_slab_unreclaimable():
    _Return_Keyword_Exception_Memo("Unclaimable Memory Slab")._meminfo_keyword_exeption()


# kernel stack memory
def test_mock_mem_kernel_stack(mocker):
    _Mock_Function()._mock_meminfo_func(mocker)
    assert memory.mem_kernel_stack() == _Mock_Function().mocked_value

def test_notfile_exception_mem_kernel_stack():
    _Return_Notfile_Exception_Memo("KernelStack", "Kernel Stack Memory")._notfile_meminfo_exception()

def test_keyword_exception_mem_kernel_stack():
    _Return_Keyword_Exception_Memo("Kernel Stack Memory")._meminfo_keyword_exeption()
