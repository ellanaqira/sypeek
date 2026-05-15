import pytest
from unittest.mock import patch

from sypeek import bios

def _mock_bios_funct(mocker_plugin, mocked_value: str):
    mocked_function = mocker_plugin.patch("sypeek.bios._get_bios_info")
    mocked_function.return_value = mocked_value


def _exc_bios_funct(keyword_error: str):
    exception_msg: str = f"Couldn't get '{keyword_error}' information"

    with patch("sypeek.board._get_board_info", side_effect=bios.BIOSInfoError(exception_msg)):
        with pytest.raises(bios.BIOSInfoError) as excinfo:
            bios._get_bios_info("file_name", keyword_error)
        assert excinfo.value.message == exception_msg



# bios vendor
def test_mock_bios_vendor(mocker):
    mocked_vendor: str = "bios vendor"
    _mock_bios_funct(mocker, mocked_vendor)
    assert bios.bios_vendor() == mocked_vendor

def test_exception_bios_vendor():
    _exc_bios_funct("BIOS Vendor")


# bios date
def test_mock_bios_date(mocker):
    mocked_date: str = "32/13/3000"
    _mock_bios_funct(mocker, mocked_date)
    assert bios.bios_date() == mocked_date

def test_exception_bios_date():
    _exc_bios_funct("BIOS Date")


# bios version
def test_mock_bios_version(mocker):
    mocked_version = "1.0"
    _mock_bios_funct(mocker, mocked_version)
    assert bios.bios_version() == mocked_version
    
def test_exception_bios_version():
    _exc_bios_funct("BIOS Version")