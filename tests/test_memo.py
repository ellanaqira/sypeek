import pytest
from unittest.mock import patch

from sypeek import memory


class _Return_Notfile_Exception_Memo:
    def __init__ (self, keyword, keyword_error):
        self.keyword = keyword
        self.keyword_error = keyword_error

    # simulate if the meminfo file doesn't exist so it returns an exception
    def _notfile_meminfo_exception(self):
        exception_msg: str = f"Couldn't get '{self.keyword_error}' information"

        @patch("builtins.open", side_effect=memory.MemoInfoError(exception_msg))
        
        def _inside(mocked_file):
            with pytest.raises(memory.MemoInfoError, match=exception_msg):
                memory._get_memo_data_meminfo(self.keyword, self.keyword_error)
        _inside()
        


class _Return_Keyword_Exception_Memo:
    def __init__(self, keyword_error: str):
        self.keyword_error = keyword_error

    # simulate if the keyword from meminfo file doesn't exist so it returns an exception
    def _meminfo_keyword_exeption(self):
        with pytest.raises(memory.MemoInfoError) as excinfo:
            memory._get_memo_data_meminfo("invalid_keyword", self.keyword_error)
        assert str(excinfo.value) == f"Couldn't get '{self.keyword_error}' information"


    # simulate if the keyword from free command doesn't exist so it returns an exception
    def _free_keyword_exeption(self):
        with pytest.raises(memory.MemoInfoError) as excinfo:
            memory._get_memo_data_free("invalid_keyword", self.keyword_error)
        assert str(excinfo.value) == f"Couldn't get '{self.keyword_error}' information"



class _Mock_Function:
    # mock the return value
    def __init__(self):
        self.mocked_value: int = 1999999.999

    def _mock_meminfo_func(self, mocker_plugin):
        mock_meminfo_func = mocker_plugin.patch("sypeek.memory._get_memo_data_meminfo")
        mock_meminfo_func.return_value = self.mocked_value

    def _mock_free_func(self, mocker_plugin):
        mock_free_func = mocker_plugin.patch("sypeek.memory._get_memo_data_free")
        mock_free_func.return_value = self.mocked_value



# General Memory ===============================================

# total memory
def test_mock_mem_total(mocker):
    _Mock_Function()._mock_meminfo_func(mocker)
    assert memory.mem_total() == _Mock_Function().mocked_value

def test_notfile_exception_mem_total():
    _Return_Notfile_Exception_Memo("MemTotal", "Total Memory")._notfile_meminfo_exception()

def test_keyword_exception_mem_total():
    _Return_Keyword_Exception_Memo("Total Memory")._meminfo_keyword_exeption()