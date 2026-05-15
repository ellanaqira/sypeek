import pytest
from unittest.mock import patch

from sypeek import board

def _mock_board_funct(mocker_plugin, mocked_value: str):
    mocked_function = mocker_plugin.patch("sypeek.board._get_board_info")
    mocked_function.return_value = mocked_value


def _exc_board_funct(keyword_error: str):
    exception_msg: str = f"Couldn't get '{keyword_error}' information"

    with patch("sypeek.board._get_board_info", side_effect=board.BoardInfoError(exception_msg)):
        with pytest.raises(board.BoardInfoError) as excinfo:
            board._get_board_info("file_name", keyword_error)
        assert excinfo.value.message == exception_msg



# board name
def test_mock_board_name(mocker):
    mocked_name: str = "Motherboard"
    _mock_board_funct(mocker, mocked_name)
    assert board.board_name() == mocked_name

def test_exception_board_name():
    _exc_board_funct("Board Name")


# board vendor
def test_mock_board_vendor(mocker):
    mocked_vendor: str = "Motherboard Vendor"
    _mock_board_funct(mocker, mocked_vendor)
    assert board.board_vendor() == mocked_vendor

def test_exception_board_vendor():
    _exc_board_funct("Board Vendor")


# board version
def test_board_version(mocker):
    mocked_version = "1.0"
    _mock_board_funct(mocker, mocked_version)
    assert board.board_version() == mocked_version
    
def test_exception_board_version():
    _exc_board_funct("Board Version")
