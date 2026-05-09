import pytest
from sypeek import cpu


class _Return_Exception():
    def __init__(self, command: str, keyword: str, keyword_error: str):
        self.command = command
        self.keyword = keyword
        self.keyword_error = keyword_error

    def _return_exception(self):
        with pytest.raises(cpu.CPUInfoError) as excinfo:
            cpu._get_data(self.command, self.keyword, self.keyword_error)
        assert str(excinfo.value) == f"Couldn't get cpu '{self.keyword_error}' information"



# Get CPU Vendor Test ==========================================

def test_get_cpu_vendor():
    assert cpu.cpu_vendor() == "AMD"

def test_cpu_vendor_not_found(mocker):
    # test cpu_vendor fuction to return "not found message" when the cpu vendor cannot be found

    mocked_name = "unknown_cpu"
    cpu_vendor_mock = mocker.patch("sypeek.cpu.cpu_vendor")
    cpu_vendor_mock.return_value = f"vendor name of '{mocked_name}' could not be found"

    assert cpu.cpu_vendor() == f"vendor name of '{mocked_name}' could not be found"
    

"""
test the cpu_vendor function to return an exception when arguments
in command and/or keyword parameters are problematic

the function below is represents the conditions when a problem occurs
when the code contains problematic command and/or keyword is executed
"""

def test_wrong_command_cpu_vendor():
    wrong_command = "wrong_lscpu"

    wrong_com_exc = _Return_Exception(wrong_command, "Vendor ID", "Vendor")
    wrong_com_exc._return_exception()


def test_wrong_keyword_cpu_vendor():
    wrong_keyword = "wrong_vendor"
    
    wrong_keyw_exc = _Return_Exception("lscpu", wrong_keyword, "Vendor")
    wrong_keyw_exc._return_exception()


def test_wrong_command_and_keyword_cpu_vendor():
    wrong_command = "wrong_lscpu"
    wrong_keyword = "wrong_vendor"
    
    wrong_com_keyw_exc = _Return_Exception(wrong_command, wrong_keyword, "Vendor")
    wrong_com_keyw_exc._return_exception()



# Get CPU Vendor ID Test =======================================

def test_get_cpu_vendorid():
    assert cpu.cpu_vendorid() == "AuthenticAMD"


"""
test the cpu_vendorid function to return an exception when arguments
in command and/or keyword parameters are problematic

the function below is represents the conditions when a problem occurs
when the code contains problematic command and/or keyword is executed
"""

def test_wrong_command_cpu_vendorid():
    wrong_command = "wrong_lscpu"
    
    wrong_com_exc = _Return_Exception(wrong_command, "Vendor ID", "Vendor ID")
    wrong_com_exc._return_exception()


def test_wrong_keyword_cpu_vendorid():
    wrong_keyword = "wrong_vendor"
    
    wrong_keyw_exc = _Return_Exception("lscpu", wrong_keyword, "Vendor ID")
    wrong_keyw_exc._return_exception()


def test_wrong_command_and_keyword_cpu_vendorid():
    wrong_command = "wrong_lscpu"
    wrong_keyword = "wrong_vendor"
    
    wrong_com_keyw_exc = _Return_Exception(wrong_command, wrong_keyword, "Vendor ID")
    wrong_com_keyw_exc._return_exception()



# Get CPU Name Test ============================================

def test_get_cpu_name():
    assert cpu.cpu_name() == "AMD Ryzen 5 3500U with Radeon Vega Mobile Gfx"


"""
test the cpu_name function to return an exception when arguments
in command and/or keyword parameters are problematic

the function below is represents the conditions when a problem occurs
when the code contains problematic command and/or keyword is executed
"""


def test_wrong_command_cpu_name():
    wrong_command = "wrong_lscpu"
    
    wrong_com_exc = _Return_Exception(wrong_command, "Model name", "Model Name")
    wrong_com_exc._return_exception()


def test_wrong_keyword_cpu_name():
    wrong_keyw = "wrong_model_name"
    
    wrong_com_exc = _Return_Exception("lscpu", wrong_keyw, "Model Name")
    wrong_com_exc._return_exception()


def test_wrong_command_keyword_cpu_name():
    wrong_command = "wrong_lscpu"
    wrong_keyw = "wrong_model_name"
    
    wrong_com_exc = _Return_Exception(wrong_command, wrong_keyw, "Model Name")
    wrong_com_exc._return_exception()



# Get CPU Thread Test ==========================================

def test_get_cpu_threads():
    assert cpu.cpu_threads() == 2


"""
test the cpu_threads function to return an exception when arguments
in command and/or keyword parameters are problematic

the function below is represents the conditions when a problem occurs
when the code contains problematic command and/or keyword is executed
"""

def test_wrong_command_cpu_threads():
    wrong_command = "wrong_lscpu"
    
    wrong_com_exc = _Return_Exception(wrong_command, "Thread", "Thread")
    wrong_com_exc._return_exception()


def test_wrong_keyword_cpu_threads():
    wrong_keyw = "wrong_thread"
    
    wrong_com_exc = _Return_Exception("lscpu", wrong_keyw, "Thread")
    wrong_com_exc._return_exception()


def test_wrong_command_keyword_cpu_threads():
    wrong_command = "wrong_lscpu"
    wrong_keyw = "wrong_thread"
    
    wrong_com_exc = _Return_Exception(wrong_command, wrong_keyw, "Thread")
    wrong_com_exc._return_exception()



# Get CPU Cores Test ===========================================

def test_get_cpu_cores():
    assert cpu.cpu_cores('l') == 8 # logical core(s)
    assert cpu.cpu_cores('L') == 8
    assert cpu.cpu_cores('p') == 4 # physical core(s)
    assert cpu.cpu_cores('P') == 4

def test_get_cpu_cores_error():
    assert cpu.cpu_cores('q') == "core must be 'l' or 'p'"
    assert cpu.cpu_cores(3) == "core must be 'l' or 'p'"
    assert cpu.cpu_cores(3.4) == "core must be 'l' or 'p'"
    assert cpu.cpu_cores(True) == "core must be 'l' or 'p'"


"""
test the cpu_cores function to return an exception when arguments
in command and/or keyword parameters are problematic

the function below is represents the conditions when a problem occurs
when the code contains problematic command and/or keyword is executed
"""

# Logical cores
    
def test_wrong_command_cpu_logical_cores():
    if cpu.cpu_cores('l') or cpu.cpu_cores('L'):
        wrong_command = "wrong_lscpu"
        
        wrong_com_exc = _Return_Exception(wrong_command, "Core(s) per socket", "Logical Core")
        wrong_com_exc._return_exception()

def test_wrong_keyword_cpu_logical_cores():
    if cpu.cpu_cores('l') or cpu.cpu_cores('L'):
        wrong_keyw = "wrong_core"
        
        wrong_com_exc = _Return_Exception("lscpu", wrong_keyw, "Logical Core")
        wrong_com_exc._return_exception()

def test_wrong_command_keyword_cpu_logical_cores():
    if cpu.cpu_cores('l') or cpu.cpu_cores('L'):
        wrong_command = "wrong_lscpu"
        wrong_keyw = "wrong_core"
        
        wrong_com_exc = _Return_Exception(wrong_command, wrong_keyw, "Logical Core")
        wrong_com_exc._return_exception()


# Physical Core

def test_wrong_command_cpu_physical_cores():
    if cpu.cpu_cores('p') or cpu.cpu_cores('P'):
        wrong_command = "wrong_lscpu"
        
        wrong_com_exc = _Return_Exception(wrong_command, "Core(s) per socket", "Physical Core")
        wrong_com_exc._return_exception()

def test_wrong_keyword_cpu_physical_cores():
    if cpu.cpu_cores('p') or cpu.cpu_cores('P'):
        wrong_keyw = "wrong_core"
        
        wrong_com_exc = _Return_Exception("lscpu", wrong_keyw, "Physical Core")
        wrong_com_exc._return_exception()

def test_wrong_command_keyword_cpu_physical_cores():
    if cpu.cpu_cores('p') or cpu.cpu_cores('P'):
        wrong_command = "wrong_lscpu"
        wrong_keyw = "wrong_core"
        
        wrong_com_exc = _Return_Exception(wrong_command, wrong_keyw, "Physical Core")
        wrong_com_exc._return_exception()



# Get CPU Family ===============================================

def test_get_cpu_family():
    assert cpu.cpu_family() == "0xf (15)"


"""
test the cpu_family function to return an exception when arguments
in command and/or keyword parameters are problematic

the function below is represents the conditions when a problem occurs
when the code contains problematic command and/or keyword is executed
"""

def test_wrong_command_cpu_family():
    wrong_command = "wrong_cpuid"
    
    wrong_com_exc = _Return_Exception(wrong_command, "family", "Family")
    wrong_com_exc._return_exception()


def test_wrong_keyword_cpu_family():
    wrong_keyw = "wrong_family"
    
    wrong_com_exc = _Return_Exception("cpuid", wrong_keyw, "Family")
    wrong_com_exc._return_exception()


def test_wrong_command_keyword_cpu_family():
    wrong_command = "wrong_cpuid"
    wrong_keyw = "wrong_family"
    
    wrong_com_exc = _Return_Exception(wrong_command, wrong_keyw, "Family")
    wrong_com_exc._return_exception()



# Get CPU Family Synth =========================================

def test_get_cpu_family_synth():
    assert cpu.cpu_family_synth() == "0x17 (23)"


"""
test the cpu_family_synth function to return an exception when arguments
in command and/or keyword parameters are problematic

the function below is represents the conditions when a problem occurs
when the code contains problematic command and/or keyword is executed
"""

def test_wrong_command_cpu_family_synth():
    wrong_command = "wrong_cpuid"
    
    wrong_com_exc = _Return_Exception(wrong_command, "family synth", "Family Synth")
    wrong_com_exc._return_exception()


def test_wrong_keyword_cpu_family_synth():
    wrong_keyw = "wrong_family_synth"
    
    wrong_com_exc = _Return_Exception("cpuid", wrong_keyw, "Family Synth")
    wrong_com_exc._return_exception()


def test_wrong_command_keyword_cpu_family_synth():
    wrong_command = "wrong_cpuid"
    wrong_keyw = "wrong_family_synth"
    
    wrong_com_exc = _Return_Exception(wrong_command, wrong_keyw, "Family Synth")
    wrong_com_exc._return_exception()



# Get CPU Model ================================================

def test_get_cpu_model():
    assert cpu.cpu_model() == "0x8 (8)"


"""
test the cpu_family_synth function to return an exception when arguments
in command and/or keyword parameters are problematic

the function below is represents the conditions when a problem occurs
when the code contains problematic command and/or keyword is executed
"""

def test_wrong_command_cpu_model():
    wrong_command = "wrong_cpuid"
    
    wrong_com_exc = _Return_Exception(wrong_command, "model", "Model")
    wrong_com_exc._return_exception()


def test_wrong_keyword_cpu_model():
    wrong_keyw = "wrong_model"
    
    wrong_com_exc = _Return_Exception("cpuid", wrong_keyw, "Model")
    wrong_com_exc._return_exception()


def test_wrong_command_keyword_cpu_model():
    wrong_command = "wrong_cpuid"
    wrong_keyw = "wrong_model"
    
    wrong_com_exc = _Return_Exception(wrong_command, wrong_keyw, "Model")
    wrong_com_exc._return_exception()



# Get CPU Model Synth ==========================================

def test_get_cpu_model_synth():
    assert cpu.cpu_model_synth() == "0x18 (24)"


def test_get_cpu_family_synth():
    assert cpu.cpu_family_synth() == "0x17 (23)"


"""
test the cpu_model_synth function to return an exception when arguments
in command and/or keyword parameters are problematic

the function below is represents the conditions when a problem occurs
when the code contains problematic command and/or keyword is executed
"""

def test_wrong_command_cpu_model_synth():
    wrong_command = "wrong_cpuid"
    
    wrong_com_exc = _Return_Exception(wrong_command, "family synth", "Model Synth")
    wrong_com_exc._return_exception()


def test_wrong_keyword_cpu_model_synth():
    wrong_keyw = "wrong_model_synth"
    
    wrong_com_exc = _Return_Exception("cpuid", wrong_keyw, "Model Synth")
    wrong_com_exc._return_exception()


def test_wrong_command_keyword_cpu_model_synth():
    wrong_command = "wrong_cpuid"
    wrong_keyw = "wrong_model_synth"
    
    wrong_com_exc = _Return_Exception(wrong_command, wrong_keyw, "Model Synth")
    wrong_com_exc._return_exception()



# Get CPU Model Synth ==========================================

def test_get_cpu_stepping():
    assert cpu.cpu_stepping() == 1


def test_get_cpu_speed():
    assert cpu.cpu_speed(0)
    assert cpu.cpu_speed(1)
    assert cpu.cpu_speed(2)
    assert cpu.cpu_speed(3)
    assert cpu.cpu_speed(4)
    assert cpu.cpu_speed(5)
    assert cpu.cpu_speed(6)
    assert cpu.cpu_speed(7)

def test_get_cpu_speed_error():
    assert cpu.cpu_speed(8) == "core number must be int() and between 0 and 7"
    assert cpu.cpu_speed(3.0) == "core number must be int() and between 0 and 7"
    assert cpu.cpu_speed('3') == "core number must be int() and between 0 and 7"
    assert cpu.cpu_speed(True) == "core number must be int() and between 0 and 7"


def test_get_cpu_temperature():
    assert cpu.cpu_temp('c')
    assert cpu.cpu_temp('C')
    assert cpu.cpu_temp('f')
    assert cpu.cpu_temp('F')
    assert cpu.cpu_temp('k')
    assert cpu.cpu_temp('K')

def test_get_cpu_temperature_error():
    assert cpu.cpu_temp('x') == "temperature scale must be 'c', 'f', or 'k'"
    assert cpu.cpu_temp(2) == "temperature scale must be 'c', 'f', or 'k'"
    assert cpu.cpu_temp(2.0) == "temperature scale must be 'c', 'f', or 'k'"
    assert cpu.cpu_temp(True) == "temperature scale must be 'c', 'f', or 'k'"


def test_cpu_cache_level1():
    assert cpu.cpu_l1c('d') == 32768
    assert cpu.cpu_l1c('D') == 32768
    assert cpu.cpu_l1c('i') == 65536
    assert cpu.cpu_l1c('I') == 65536

def test_cpu_cache_level_l1_error():
    assert cpu.cpu_l1c('h') == "cache type must be 'd' or 'i'"
    assert cpu.cpu_l1c(5) == "cache type must be 'd' or 'i'"
    assert cpu.cpu_l1c(5.0) == "cache type must be 'd' or 'i'"
    assert cpu.cpu_l1c(True) == "cache type must be 'd' or 'i'"


def test_cpu_cache_level2():
    assert cpu.cpu_l2c() == 524288

def test_cpu_cache_level3():
    assert cpu.cpu_l3c() == 4194304
