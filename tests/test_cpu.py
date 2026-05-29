import pytest
from unittest.mock import patch

from sypeek import cpu


class _Mocked_Cpu_Func:
    def __init__(self, mocked_value):
        self.mocked_value = mocked_value

    def _mock_cpu_get_data_from_command(self, mocker_plugin):
        mocker_plugin.patch("sypeek.cpu._get_cpu_data_from_command").return_value = self.mocked_value

    def _mock_cpu_get_data_from_cpuinfo(self, mocker_plugin):
        mocker_plugin.patch("sypeek.cpu._get_cpu_data_from_cpuinfo").return_value = self.mocked_value


class _Return_Exception:
    """
    test the cpu function to return an exception when the code
    contains problematic command and/or keyword is executed
    """

    def __init__(self, keyword_error: str,  command: str = ""):
        self.command = command
        self.keyword = "invalid keyword"
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
        


# _get_cpu_data_from_cpuinfo function ==============================================================

# Get CPU Cores Test
def test_mock_cpu_cores(mocker):
    dummy_core_number: int = 4
    mocked_get_cpu_cores = _Mocked_Cpu_Func(dummy_core_number)
    mocked_get_cpu_cores._mock_cpu_get_data_from_cpuinfo(mocker)

    assert cpu.cpu_cores('l') == dummy_core_number # logical core(s)
    assert cpu.cpu_cores('p') == dummy_core_number # physical core(s)

def test_mock_cpu_cores_error():
    assert cpu.cpu_cores('q') == "core type must be 'l' or 'p'"

# return an exception 
# Logical cores    
def test_exception_cpu_logical_cores():
    cpu_cores_exception = _Return_Exception("Logical Core")
    cpu_cores_exception._return_get_data_cpuinfo_exception()

# Physical Core
def test_exception_cpu_physical_cores():
    cpu_cores_exception = _Return_Exception("Physical Core")
    cpu_cores_exception._return_get_data_cpuinfo_exception()



# Get CPU Vendor Test
def test_mock_cpu_vendor(mocker):
    dummy_vendor: dict = {"vendor id" : "GenuineIntel", "vendor" : "Intel"}
    mocked_cpu_vendor = _Mocked_Cpu_Func(dummy_vendor["vendor id"])
    mocked_cpu_vendor._mock_cpu_get_data_from_cpuinfo(mocker)
    assert cpu.cpu_vendor() == dummy_vendor["vendor"]

def test_mock_cpu_vendor_not_found(mocker):
    # test cpu_vendor fuction to return "not found message" when the cpu vendor cannot be found
    unknown_vendor = "Unknown_CPU"
    mocked_cpu_vendor = _Mocked_Cpu_Func(unknown_vendor)
    mocked_cpu_vendor._mock_cpu_get_data_from_cpuinfo(mocker)
    assert cpu.cpu_vendor() == f"vendor name of '{unknown_vendor}' could not be found"

# return an exception 
def test_exception_cpu_vendor():
    cpu_vendor_exception = _Return_Exception("Vendor")
    cpu_vendor_exception._return_get_data_cpuinfo_exception()



# Get CPU Vendor ID Test
def test_mock_cpu_vendorid(mocker):
    dummy_vendorid: str = "NexGenDriven"
    mocked_cpu_vendorid = _Mocked_Cpu_Func(dummy_vendorid)
    mocked_cpu_vendorid._mock_cpu_get_data_from_cpuinfo(mocker)
    assert cpu.cpu_vendorid() == dummy_vendorid

# return an exception 
def test_exception_cpu_vendorid():
    cpu_vendorid_exception = _Return_Exception("Vendor ID")
    cpu_vendorid_exception._return_get_data_cpuinfo_exception()



# Get CPU Model Name Test
def test_mock_cpu_name(mocker):
    dummy_cpu_name: str = "Intel Core i5 7200u"
    mocked_cpu_name = _Mocked_Cpu_Func(dummy_cpu_name)
    mocked_cpu_name._mock_cpu_get_data_from_cpuinfo(mocker)
    assert cpu.cpu_model_name() == dummy_cpu_name

# return an exception 
def test_exception_cpu_name():
    cpu_name_exception = _Return_Exception("Model Name")
    cpu_name_exception._return_get_data_cpuinfo_exception()



# Get CPU Stepping Test
def test_mock_cpu_stepping(mocker):
    dummy_cpu_stepping: int = 1
    mocked_cpu_stepping = _Mocked_Cpu_Func(dummy_cpu_stepping)
    mocked_cpu_stepping._mock_cpu_get_data_from_cpuinfo(mocker)
    assert cpu.cpu_stepping() == dummy_cpu_stepping

# return an exception 
def test_exception_cpu_stepping():
    cpu_stepping_exception = _Return_Exception("Stepping")
    cpu_stepping_exception._return_get_data_cpuinfo_exception()



# Get CPU Speed Test
def test_mock_cpu_speed(mocker):
    dummy_cpu_speed: float = 1999.999
    mocked_cpu_speed = _Mocked_Cpu_Func(dummy_cpu_speed)
    mocked_cpu_speed._mock_cpu_get_data_from_cpuinfo(mocker)
    assert cpu.cpu_speed(0) == dummy_cpu_speed
    assert cpu.cpu_speed(1) == dummy_cpu_speed
    assert cpu.cpu_speed(2) == dummy_cpu_speed
    assert cpu.cpu_speed(3) == dummy_cpu_speed

def test_mock_cpu_speed_error(mocker):
    dummy_error_message: str = "core number must be int() and between 0 and 3"
    mocker.patch("sypeek.cpu.cpu_speed").return_value = dummy_error_message
    assert cpu.cpu_speed(4) == dummy_error_message
    assert cpu.cpu_speed('3') == dummy_error_message

# return an exception 
def test_exception_cpu_speed():
    cpu_speed_exception = _Return_Exception("Speed")
    cpu_speed_exception._return_get_data_cpuinfo_exception()



# _get_cpu_data_from_command function ==============================================================

# Get CPU Thread Test
def test_mock_cpu_threads(mocker):
    dummy_thread: int = 2
    mocked_cpu_threads = _Mocked_Cpu_Func(dummy_thread)
    mocked_cpu_threads._mock_cpu_get_data_from_command(mocker)
    assert cpu.cpu_threads() == dummy_thread

# return an exception 
def test_exception_cpu_threads():
    cpu_threads_exception = _Return_Exception("Thread", "lscpu")
    cpu_threads_exception._return_get_data_command_exception()


# Get CPU Family Test
def test_mock_cpu_family(mocker):
    dummy_cpu_family: str = "0xf (15)"
    mocked_cpu_family = _Mocked_Cpu_Func(dummy_cpu_family)
    mocked_cpu_family._mock_cpu_get_data_from_command(mocker)
    assert cpu.cpu_family() == dummy_cpu_family

# return an exception 
def test_exception_wrong_keyword_cpu_family():
    cpu_family_exception = _Return_Exception("Family", "cpuid")
    cpu_family_exception._return_get_data_command_exception()


# Get CPU Family Synth Test
def test_mock_cpu_family_synth(mocker):
    dummy_cpu_family_synth: str = "0x17 (23)"
    mocked_cpu_family_synth = _Mocked_Cpu_Func(dummy_cpu_family_synth)
    mocked_cpu_family_synth._mock_cpu_get_data_from_command(mocker)
    assert cpu.cpu_family_synth() == dummy_cpu_family_synth

# return an exception 
def test_exception_cpu_family_synth():
    cpu_family_synth_exception = _Return_Exception("Family Synth", "cpuid")
    cpu_family_synth_exception._return_get_data_command_exception()


# Get CPU Model Test
def test_mock_cpu_model(mocker):
    dummy_cpu_model = "0x8 (8)"
    mocked_cpu_model = _Mocked_Cpu_Func(dummy_cpu_model)
    mocked_cpu_model._mock_cpu_get_data_from_command(mocker)
    assert cpu.cpu_model() == dummy_cpu_model

# return an exception 
def test_exception_cpu_model():
    cpu_model_exception = _Return_Exception("Model", "cpuid")
    cpu_model_exception._return_get_data_command_exception()


# Get CPU Model Synth
def test_mock_cpu_model_synth(mocker):
    dummy_cpu_model_synth: str = "0x18 (24)"
    mocked_cpu_model_synth = _Mocked_Cpu_Func(dummy_cpu_model_synth)
    mocked_cpu_model_synth._mock_cpu_get_data_from_command(mocker)
    assert cpu.cpu_model_synth() == dummy_cpu_model_synth

# return an exception 
def test_exception_cpu_model_synth():    
    cpu_model_synth_exception = _Return_Exception("Model Synth", "cpuid")
    cpu_model_synth_exception._return_get_data_command_exception()



# Get CPU Temperature
def mock_cpu_temp(mocker_plugin, cpu_parameter, dummy_value):
    mocker_plugin.patch("sypeek.cpu.cpu_temp").return_value = dummy_value
    assert cpu.cpu_temp(cpu_parameter) == dummy_value

def test_mock_cpu_temperature(mocker):
    mock_cpu_temp(mocker, 'c', 64.8)
    mock_cpu_temp(mocker, 'f', 64.8)
    mock_cpu_temp(mocker, 'k', 64.8)

def test_mock_cpu_temperature_error():
    assert cpu.cpu_temp('x') == "temperature scale must be 'c', 'f', or 'k'"

# return an exception 
def test_exception_cpu_temperature():
    cpu_temperature_exception = _Return_Exception("Temperature", "sensors")
    cpu_temperature_exception._return_get_data_command_exception()



# _get_cpu_cache_level function ====================================================================

# return _get_level_cache exception
def _return_cache_level_exception(order: int, keyword_error: str):
    invalid_keyword: str = "wrong_keyword"
    with pytest.raises(cpu.CPUInfoError) as excinfo:
        cpu._get_cpu_cache_info(order, invalid_keyword, keyword_error, )
    assert excinfo.value.message == f"Couldn't get cpu '{keyword_error}' information"

# Get CPU Cache Level 1 Test
def test_mock_cpu_cache_l1(mocker):
    mock_cpu_cache_level: int = 45555
    mocker.patch("sypeek.cpu.cpu_l1c", return_value = mock_cpu_cache_level)
    assert cpu.cpu_l1c('d') == mock_cpu_cache_level
    assert cpu.cpu_l1c('i') == mock_cpu_cache_level

def test_mock_cpu_cache_l1_error():
    assert cpu.cpu_l1c('h') == "cache type must be 'd' or 'i'"

# return an exception 
def test_exception_cpu_cache_l1_data():
    _return_cache_level_exception(0, "Data Cache Level 1")

def test_exception_cpu_cache_l1_instruction():
    _return_cache_level_exception(1, "Instruction Cache Level 1")


# Get CPU Cache Level 2 Test
def test_mock_cpu_cache_l2(mocker):
    mock_cpu_cache_level = 45555
    mocker.patch("sypeek.cpu.cpu_l2c", return_value = mock_cpu_cache_level)
    assert cpu.cpu_l2c() == mock_cpu_cache_level

# return an exception 
def test_exception_cpu_cache_l2():
    _return_cache_level_exception(2, "Cache Level 2")


# Get CPU Cache Level 3 Test
def test_mock_cpu_cache_l3(mocker):
    mock_cpu_cache_level = 45555
    mocker.patch("sypeek.cpu.cpu_l3c", return_value = mock_cpu_cache_level)
    assert cpu.cpu_l3c() == mock_cpu_cache_level

# return an exception 
def test_exception_cpu_cache_l3():
    _return_cache_level_exception(3, "Cache Level 3")