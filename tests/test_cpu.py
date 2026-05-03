import pytest
from sypeek import cpu


def test_get_cpu_vendor():
    assert cpu.cpu_vendor() == "AMD"

def test_get_cpu_vendorid():
    assert cpu.cpu_vendorid() == "AuthenticAMD"

def test_get_cpu_name():
    assert cpu.cpu_name() == "AMD Ryzen 5 3500U with Radeon Vega Mobile Gfx"

def test_get_cpu_threads():
    assert cpu.cpu_threads() == 2


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
    

def test_get_cpu_family():
    assert cpu.cpu_family() == "0xf (15)"

def test_get_cpu_family_synth():
    assert cpu.cpu_family_synth() == "0x17 (23)"

def test_get_cpu_model():
    assert cpu.cpu_model() == "0x8 (8)"

def test_get_cpu_model_synth():
    assert cpu.cpu_model_synth() == "0x18 (24)"

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
