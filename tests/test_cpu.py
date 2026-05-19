import pytest
from unittest.mock import patch

from sypeek import cpu


class _Return_Exception:
    """
    test the cpu function to return an exception when the code
    contains problematic command and/or keyword is executed
    """

    def __init__(self, command: str, keyword: str, keyword_error: str):
        self.command = command
        self.keyword = keyword
        self.keyword_error = keyword_error
        self.exception_msg: str = f"Couldn't get cpu '{self.keyword_error}' information"

    def _return_get_data_cpuinfo_exception(self):
        with patch("sypeek.cpu._get_cpu_data_from_cpuinfo", side_effect=cpu.CPUInfoError(self.exception_msg)):
            with pytest.raises(cpu.CPUInfoError) as excinfo:
                cpu._get_cpu_data_from_cpuinfo(self.command, self.keyword, self.keyword_error)
            assert excinfo.value.message == self.exception_msg

    def _return_get_data_command_exception(self):
        with patch("sypeek.cpu._get_cpu_data_from_command", side_effect=cpu.CPUInfoError(self.exception_msg)):
            with pytest.raises(cpu.CPUInfoError) as excinfo:
                cpu._get_cpu_data_from_command(self.command, self.keyword, self.keyword_error)
            assert excinfo.value.message == self.exception_msg
            


class _Mocked_Cpu_Func:
    def __init__(self, mocked_value):
        self.mocked_value = mocked_value

    def _mock_cpu_get_data_from_command(self, mocker_plugin):
        mocker_plugin.patch("sypeek.cpu._get_cpu_data_from_command").return_value = self.mocked_value

    def _mock_cpu_get_data_from_cpuinfo(self, mocker_plugin):
        mocker_plugin.patch("sypeek.cpu._get_cpu_data_from_cpuinfo").return_value = self.mocked_value

    def _mock_cpu_cache_level(self, mocker_plugin):
        mocker_plugin.patch("sypeek.cpu._get_cpu_cache_level").return_value = self.mocked_value



# _get_cpu_data_from_cpuinfo function ==============================================================

# Get CPU Cores Test
def test_get_cpu_cores():
    assert cpu.cpu_cores('l') == 8 # logical core(s)
    assert cpu.cpu_cores('L') == 8
    assert cpu.cpu_cores('p') == 4 # physical core(s)
    assert cpu.cpu_cores('P') == 4

def test_get_cpu_cores_error():
    assert cpu.cpu_cores('q') == "core type must be 'l' or 'p'"
    assert cpu.cpu_cores(3) == "core type must be 'l' or 'p'"
    assert cpu.cpu_cores(3.4) == "core type must be 'l' or 'p'"
    assert cpu.cpu_cores(True) == "core type must be 'l' or 'p'"

# return an exception 
# Logical cores    
def test_wrong_command_cpu_logical_cores():
    wrong_com_exc = _Return_Exception("wrong_lscpu", "Core(s) per socket", "Logical Core")
    wrong_com_exc._return_get_data_cpuinfo_exception()

def test_wrong_keyword_cpu_logical_cores():
    wrong_com_exc = _Return_Exception("lscpu", "wrong_core", "Logical Core")
    wrong_com_exc._return_get_data_cpuinfo_exception()

# Physical Core
def test_wrong_command_cpu_physical_cores():
    wrong_com_exc = _Return_Exception("wrong_lscpu", "Core(s) per socket", "Physical Core")
    wrong_com_exc._return_get_data_cpuinfo_exception()

def test_wrong_keyword_cpu_physical_cores():
    wrong_com_exc = _Return_Exception("lscpu", "wrong_core", "Physical Core")
    wrong_com_exc._return_get_data_cpuinfo_exception()



# Get CPU Vendor Test
def test_get_cpu_vendor(mocker):
    mocked_value: dict = {"vendor id" : "GenuineIntel", "vendor" : "Intel"}
    _Mocked_Cpu_Func(mocked_value["vendor id"])._mock_cpu_get_data_from_cpuinfo(mocker)
    assert cpu.cpu_vendor() == mocked_value["vendor"]

def test_cpu_vendor_not_found(mocker):
    # test cpu_vendor fuction to return "not found message" when the cpu vendor cannot be found
    mocked_cpu_vendor = "Unknown_CPU"
    _Mocked_Cpu_Func(mocked_cpu_vendor)._mock_cpu_get_data_from_cpuinfo(mocker)
    assert cpu.cpu_vendor() == f"vendor name of '{mocked_cpu_vendor}' could not be found"

# return an exception 
def test_wrong_command_cpu_vendor():
    wrong_com_exc = _Return_Exception("wrong_lscpu", "Vendor ID", "Vendor")
    wrong_com_exc._return_get_data_cpuinfo_exception()

def test_wrong_keyword_cpu_vendor():
    wrong_keyw_exc = _Return_Exception("lscpu", "wrong_vendor", "Vendor")
    wrong_keyw_exc._return_get_data_cpuinfo_exception()

def test_wrong_command_and_keyword_cpu_vendor():
    wrong_com_keyw_exc = _Return_Exception("wrong_lscpu", "wrong_vendor", "Vendor")
    wrong_com_keyw_exc._return_get_data_cpuinfo_exception()



# Get CPU Vendor ID Test
def test_get_cpu_vendorid(mocker):
    mock_vendorid: str = "NexGenDriven"
    _Mocked_Cpu_Func(mock_vendorid)._mock_cpu_get_data_from_cpuinfo(mocker)
    assert cpu.cpu_vendorid() == mock_vendorid

# return an exception 
def test_wrong_command_cpu_vendorid():
    wrong_com_exc = _Return_Exception("wrong_lscpu", "Vendor ID", "Vendor ID")
    wrong_com_exc._return_get_data_cpuinfo_exception()

def test_wrong_keyword_cpu_vendorid():
    wrong_keyw_exc = _Return_Exception("lscpu", "wrong_vendor", "Vendor ID")
    wrong_keyw_exc._return_get_data_cpuinfo_exception()



# Get CPU Model Name Test
def test_get_cpu_name(mocker):
    mock_cpu_name: str = "Intel Core i5 7200u"
    _Mocked_Cpu_Func(mock_cpu_name)._mock_cpu_get_data_from_cpuinfo(mocker)
    assert cpu.cpu_model_name() == mock_cpu_name

# return an exception 
def test_wrong_command_cpu_name():    
    wrong_com_exc = _Return_Exception("wrong_lscpu", "Model name", "Model Name")
    wrong_com_exc._return_get_data_cpuinfo_exception()

def test_wrong_keyword_cpu_name():
    wrong_com_exc = _Return_Exception("lscpu", "wrong_model_name", "Model Name")
    wrong_com_exc._return_get_data_cpuinfo_exception()



# Get CPU Stepping Test
def test_get_cpu_stepping(mocker):
    mock_cpu_stepping: int = 1
    _Mocked_Cpu_Func(mock_cpu_stepping)._mock_cpu_get_data_from_cpuinfo(mocker)
    assert cpu.cpu_stepping() == mock_cpu_stepping

# return an exception 
def test_wrong_command_cpu_stepping():
    wrong_com_exc = _Return_Exception("wrong_lscpu", "Stepping", "Stepping")
    wrong_com_exc._return_get_data_cpuinfo_exception()

def test_wrong_keyword_cpu_stepping():
    wrong_com_exc = _Return_Exception("lscpu", "wrong_stepping", "Stepping")
    wrong_com_exc._return_get_data_cpuinfo_exception()



# Get CPU Speed Test
def test_get_cpu_speed(mocker):
    mocked_speed: float = 1999.999
    _Mocked_Cpu_Func(mocked_speed)._mock_cpu_get_data_from_cpuinfo(mocker)
    assert cpu.cpu_speed(0) == mocked_speed
    assert cpu.cpu_speed(1) == mocked_speed
    assert cpu.cpu_speed(2) == mocked_speed
    assert cpu.cpu_speed(3) == mocked_speed

def test_get_cpu_speed_error(mocker):
    mocked_speed_error: str = "core number must be int() and between 0 and 4"
    _Mocked_Cpu_Func(mocked_speed_error)._mock_cpu_get_data_from_cpuinfo(mocker)
    assert cpu.cpu_speed(4) == mocked_speed_error
    assert cpu.cpu_speed(3.0) == mocked_speed_error
    assert cpu.cpu_speed('3') == mocked_speed_error
    assert cpu.cpu_speed(True) == mocked_speed_error

# return an exception 
def test_cpu_speed_exception():
    exc_message: str = "Couldn't get cpu 'Speed' information"

    with patch("sypeek.cpu.cpu_speed", side_effect=cpu.CPUInfoError(exc_message)):
        with pytest.raises(cpu.CPUInfoError) as excinfo:
            cpu.cpu_speed(0)
        assert excinfo.value.message == exc_message



# _get_cpu_data_from_command function ==============================================================

# Get CPU Thread Test
def test_get_cpu_threads(mocker):
    mock_thread: int = 2
    _Mocked_Cpu_Func(mock_thread)._mock_cpu_get_data_from_command(mocker)
    assert cpu.cpu_threads() == mock_thread

# return an exception 
def test_wrong_command_cpu_threads():
    wrong_com_exc = _Return_Exception("wrong_lscpu", "Thread", "Thread")
    wrong_com_exc._return_get_data_command_exception()

def test_wrong_keyword_cpu_threads():
    wrong_com_exc = _Return_Exception("lscpu", "wrong_thread", "Thread")
    wrong_com_exc._return_get_data_command_exception()



# Get CPU Family Test
def test_get_cpu_family(mocker):
    mock_cpu_family: str = "0xf (15)"
    _Mocked_Cpu_Func(mock_cpu_family)._mock_cpu_get_data_from_command(mocker)
    assert cpu.cpu_family() == mock_cpu_family

# return an exception 
def test_wrong_command_cpu_family():
    wrong_com_exc = _Return_Exception("wrong_cpuid", "family", "Family")
    wrong_com_exc._return_get_data_command_exception()

def test_wrong_keyword_cpu_family():
    wrong_com_exc = _Return_Exception("cpuid", "wrong_family", "Family")
    wrong_com_exc._return_get_data_command_exception()



# Get CPU Family Synth Test
def test_get_cpu_family_synth(mocker):
    mock_cpu_family_synth: str = "0x17 (23)"
    _Mocked_Cpu_Func(mock_cpu_family_synth)._mock_cpu_get_data_from_command(mocker)
    assert cpu.cpu_family_synth() == mock_cpu_family_synth

# return an exception 
def test_wrong_command_cpu_family_synth():
    wrong_com_exc = _Return_Exception("wrong_cpuid", "family synth", "Family Synth")
    wrong_com_exc._return_get_data_command_exception()

def test_wrong_keyword_cpu_family_synth():
    wrong_com_exc = _Return_Exception("cpuid", "wrong_family_synth", "Family Synth")
    wrong_com_exc._return_get_data_command_exception()



# Get CPU Model Test
def test_get_cpu_model(mocker):
    mock_cpu_model = "0x8 (8)"
    _Mocked_Cpu_Func(mock_cpu_model)._mock_cpu_get_data_from_command(mocker)
    assert cpu.cpu_model() == mock_cpu_model

# return an exception 
def test_wrong_command_cpu_model():
    wrong_com_exc = _Return_Exception("wrong_cpuid", "model", "Model")
    wrong_com_exc._return_get_data_command_exception()

def test_wrong_keyword_cpu_model():
    wrong_com_exc = _Return_Exception("cpuid", "wrong_model", "Model")
    wrong_com_exc._return_get_data_command_exception()



# Get CPU Model Synth
def test_get_cpu_model_synth(mocker):
    mock_cpu_model_synth: str = "0x18 (24)"
    _Mocked_Cpu_Func(mock_cpu_model_synth)._mock_cpu_get_data_from_command(mocker)
    assert cpu.cpu_model_synth() == mock_cpu_model_synth

# return an exception 
def test_wrong_command_cpu_model_synth():
    wrong_com_exc = _Return_Exception("wrong_cpuid", "family synth", "Model Synth")
    wrong_com_exc._return_get_data_command_exception()

def test_wrong_keyword_cpu_model_synth():    
    wrong_com_exc = _Return_Exception("cpuid", "wrong_model_synth", "Model Synth")
    wrong_com_exc._return_get_data_command_exception()



# Get CPU Temperature
def mock_cpu_temp(mocker_plugin, cpu_parameter, mocked_value):
    mocker_plugin.patch("sypeek.cpu.cpu_temp").return_value = mocked_value
    assert cpu.cpu_temp(cpu_parameter) == mocked_value

def test_get_cpu_temperature(mocker):
    mock_cpu_temp(mocker, 'c', 64.8)
    mock_cpu_temp(mocker, 'C', 64.8)
    mock_cpu_temp(mocker, 'f', 64.8)
    mock_cpu_temp(mocker, 'F', 64.8)
    mock_cpu_temp(mocker, 'k', 64.8)
    mock_cpu_temp(mocker, 'K', 64.8)    

def test_get_cpu_temperature_error():
    assert cpu.cpu_temp('x') == "temperature scale must be 'c', 'f', or 'k'"
    assert cpu.cpu_temp(2) == "temperature scale must be 'c', 'f', or 'k'"
    assert cpu.cpu_temp(2.0) == "temperature scale must be 'c', 'f', or 'k'"
    assert cpu.cpu_temp(True) == "temperature scale must be 'c', 'f', or 'k'"

# return an exception 
def test_wrong_command_cpu_temperature():
    wrong_com_exc = _Return_Exception("wrong_sensors", "Tctl", "Temperature")
    wrong_com_exc._return_get_data_command_exception()

def test_wrong_keyword_cpu_temperature():
    wrong_com_exc = _Return_Exception("sensors", "wrong_Tctl", "Temperature")
    wrong_com_exc._return_get_data_command_exception()



# _get_cpu_cache_level function ====================================================================

# return _get_level_cache exception
def _return_cache_level_exception(order: int, keyword_error: str):
    with pytest.raises(cpu.CPUInfoError) as excinfo:
        cpu._get_cpu_cache_level(order, keyword_error)
    assert excinfo.value.message == f"Couldn't get cpu '{keyword_error}' information"



# Get CPU Cache Level 1 Test
def test_cpu_cache_level1(mocker):
    mock_cpu_cache_level: int = 45555

    _Mocked_Cpu_Func(mock_cpu_cache_level)._mock_cpu_cache_level(mocker)
    assert cpu.cpu_l1c('d') == mock_cpu_cache_level
    assert cpu.cpu_l1c('D') == mock_cpu_cache_level
    assert cpu.cpu_l1c('i') == mock_cpu_cache_level
    assert cpu.cpu_l1c('I') == mock_cpu_cache_level

def test_cpu_cache_level_l1_error():
    assert cpu.cpu_l1c('h') == "cache type must be 'd' or 'i'"
    assert cpu.cpu_l1c(5) == "cache type must be 'd' or 'i'"
    assert cpu.cpu_l1c(5.0) == "cache type must be 'd' or 'i'"
    assert cpu.cpu_l1c(True) == "cache type must be 'd' or 'i'"

# return an exception 
def mock_cpu_cache_l1_data():
    _return_cache_level_exception(0, "Data Cache Level 1")

def mock_cpu_cache_l1_instruction():
    _return_cache_level_exception(1, "Instruction Cache Level 1")



# Get CPU Cache Level 2 Test
def test_cpu_cache_level2(mocker):
    mock_cpu_cache_level: int = 45555
    _Mocked_Cpu_Func(mock_cpu_cache_level)._mock_cpu_cache_level(mocker)
    assert cpu.cpu_l2c() == mock_cpu_cache_level

# return an exception 
def mock_cpu_cache_level2():
    _return_cache_level_exception(2, "Cache Level 2")



# Get CPU Cache Level 3 Test
def test_cpu_cache_level3(mocker):
    mock_cpu_cache_level: int = 45555
    _Mocked_Cpu_Func(mock_cpu_cache_level)._mock_cpu_cache_level(mocker)
    assert cpu.cpu_l3c() == mock_cpu_cache_level

# return an exception 
def mock_cpu_cache_level2():
    _return_cache_level_exception(3, "Cache Level 3")