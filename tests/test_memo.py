import pytest
from sypeek import memory


class _Return_Mem_Exception:
    def __init__(self, keyword_error: str):
        self.keyword_error = keyword_error

    def _return_mem_meminfo_exeption(self):
        with pytest.raises(memory.MemoInfoError) as excinfo:
            memory._get_memo_data_meminfo("invalid_keyword", self.keyword_error)
        assert str(excinfo.value) == f"Couldn't get '{self.keyword_error}' information"

    def _return_mem_free_exeption(self):
        with pytest.raises(memory.MemoInfoError) as excinfo:
            memory._get_memo_data_free("invalid_keyword", self.keyword_error)
        assert str(excinfo.value) == f"Couldn't get '{self.keyword_error}' information"


class _Mock_Function:
    # mock the return value
    def __init__(self, function_name):
        self.func_name = function_name

    def _mock_meminfo_func(self, mocker_plugin):
        mocked_value: int = 1999999.999

        mock_meminfo_func = mocker_plugin.patch("sypeek.memory._get_memo_data_meminfo")
        mock_meminfo_func.return_value = mocked_value

        assert lambda:self.func_name == mocked_value


    def _mock_free_func(self, mocker_plugin):
        mocked_value: int = 1999999.999

        mock_free_func = mocker_plugin.patch("sypeek.memory._get_memo_data_free")
        mock_free_func.return_value = mocked_value

        assert lambda:self.func_name == mocked_value
