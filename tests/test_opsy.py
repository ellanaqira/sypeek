import pytest
from unittest.mock import patch

from sypeek import opsy


def _mock_opsy_funct(mocker_plugin, func_instring: str, mocked_value):
    mocker_plugin.patch(f"sypeek.{func_instring}").return_value = mocked_value


def _exception_get_os_info(keyword: str, keyword_error: str):
    # return an exception for function that rely on opsy._get_os_info function
    
    exception_msg: str = f"Couldn't get '{keyword_error}' information"

    with patch("sypeek.opsy._get_os_info", side_effect=opsy.OpSyInfoError(exception_msg)):
        with pytest.raises(opsy.OpSyInfoError) as excinfo:
            opsy._get_os_info(keyword, keyword_error)
        assert excinfo.value.message == exception_msg



# test opsy.distro_name function ===============================
def test_mock_distro_name(mocker):
    mocked_value: str = "mocked distro name"
    _mock_opsy_funct(mocker, "opsy.distro_name", mocked_value)
    assert opsy.distro_name() == mocked_value

def test_exception_distro_name():
    _exception_get_os_info("NAME", "Distribution Name")



# test opsy.distro_ver function ================================
def test_mock_destro_version(mocker):
    mocked_value: str = "mocked_version"
    _mock_opsy_funct(mocker, "opsy.distro_ver", mocked_value)
    assert opsy.distro_ver() == mocked_value

def test_exception_distro_version():
    _exception_get_os_info("VERSION_ID", "Distribution Version")



# test opsy.opsy_kernel function ===============================
def test_mock_opsy_kernel(mocker):
    mocked_value: str = "mocked_kernel"
    _mock_opsy_funct(mocker, "opsy.opsy_kernel", mocked_value)
    assert opsy.opsy_kernel() == mocked_value

def test_exception_opsy_kernel():
    exception_msg: str = "Couldn't get 'Kernel Name' information"

    with patch("sypeek.opsy.opsy_kernel", side_effect=opsy.OpSyInfoError(exception_msg)):
        with pytest.raises(opsy.OpSyInfoError) as excinfo:
            opsy.opsy_kernel()
        assert excinfo.value.message == exception_msg



# test opsy.host_name function =================================
def test_mock_host_name(mocker):
    mocked_value: str = "mocked_host"
    _mock_opsy_funct(mocker, "opsy.host_name", mocked_value)
    assert opsy.host_name() == mocked_value

def test_exception_host_name():
    exception_msg: str = f"Couldn't get 'Host Name' information"

    with patch("sypeek.opsy.host_name", side_effect=opsy.OpSyInfoError(exception_msg)):
        with pytest.raises(opsy.OpSyInfoError) as excinfo:
            opsy.host_name()
        assert excinfo.value.message == exception_msg



# test opsy.up_time function ===================================
def test_mock_up_time_pretty(mocker):
    mocked_minutes_value: int = 27
    _mock_opsy_funct(mocker, "opsy.up_time", mocked_minutes_value)
    assert opsy.up_time() == mocked_minutes_value

def test_mock_up_time_minutes(mocker):
    mocked_pretty_value: str = "0 hours, 27 minutes"
    _mock_opsy_funct(mocker, "opsy.up_time", mocked_pretty_value)
    assert opsy.up_time('p') == mocked_pretty_value

def test_mock_up_time_invalid_appearance(mocker):
    mocked_invalid_appearance: str = "appearances most be 'p' or an empty string"
    _mock_opsy_funct(mocker, "opsy.up_time", mocked_invalid_appearance)
    assert opsy.up_time('x') == mocked_invalid_appearance


def test_exception_up_time():
    exception_msg: str = f"Couldn't get 'Uptime' information"

    with patch("sypeek.opsy.up_time", side_effect=opsy.OpSyInfoError(exception_msg)):
        with pytest.raises(opsy.OpSyInfoError) as excinfo:
            opsy.up_time()
        assert excinfo.value.message == exception_msg

