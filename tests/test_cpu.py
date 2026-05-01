import pytest
from sypeek import cpu


def test_get_cpu_vendor():
    assert cpu.vendor() == "AMD"

def test_get_cpu_vendorid():
    assert cpu.vendorid() == "AuthenticAMD"

def test_get_cpu_name():
    assert cpu.name() == "AMD Ryzen 5 3500U with Radeon Vega Mobile Gfx"

def test_get_cpu_threads():
    assert cpu.threads() == 2


def test_get_cpu_cores():
    assert cpu.cores('l') == 8 # logical core(s)
    assert cpu.cores('L') == 8
    assert cpu.cores('p') == 4 # physical core(s)
    assert cpu.cores('P') == 4

def test_get_cpu_cores_error():
    assert cpu.cores('q') == "core must be 'l' or 'p'"
    assert cpu.cores(3) == "core must be 'l' or 'p'"
    assert cpu.cores(3.4) == "core must be 'l' or 'p'"
    assert cpu.cores(True) == "core must be 'l' or 'p'"
    

def test_get_cpu_family():
    assert cpu.family() == "0xf (15)"

def test_get_cpu_family_synth():
    assert cpu.family_synth() == "0x17 (23)"

def test_get_cpu_model():
    assert cpu.model() == "0x8 (8)"

def test_get_cpu_model_synth():
    assert cpu.model_synth() == "0x18 (24)"

def test_get_cpu_stepping():
    assert cpu.stepping() == 1


def test_get_cpu_speed():
    assert cpu.speed(0)
    assert cpu.speed(1)
    assert cpu.speed(2)
    assert cpu.speed(3)
    assert cpu.speed(4)
    assert cpu.speed(5)
    assert cpu.speed(6)
    assert cpu.speed(7)

def test_get_cpu_speed_error():
    assert cpu.speed(8) == "core number must be between 0 and 7"
    assert cpu.speed(3.0) == "core number must be between 0 and 7"
    assert cpu.speed('3') == "core number must be between 0 and 7"
    assert cpu.speed(True) == "core number must be between 0 and 7"


def test_get_cpu_temperature():
    assert cpu.temp('c')
    assert cpu.temp('C')
    assert cpu.temp('f')
    assert cpu.temp('F')
    assert cpu.temp('k')
    assert cpu.temp('K')

def test_get_cpu_temperature_error():
    assert cpu.temp('x') == "temperature scale must be 'c', 'f', or 'k'"
    assert cpu.temp(2) == "temperature scale must be 'c', 'f', or 'k'"
    assert cpu.temp(2.0) == "temperature scale must be 'c', 'f', or 'k'"
    assert cpu.temp(True) == "temperature scale must be 'c', 'f', or 'k'"


def test_cpu_cache_level1():
    assert cpu.l1('d') == 32768
    assert cpu.l1('D') == 32768
    assert cpu.l1('i') == 65536
    assert cpu.l1('I') == 65536

def test_cpu_cache_level1_error():
    assert cpu.l1('h') == "cache type must be 'd' or 'i'"
    assert cpu.l1(5) == "cache type must be 'd' or 'i'"
    assert cpu.l1(5.0) == "cache type must be 'd' or 'i'"
    assert cpu.l1(True) == "cache type must be 'd' or 'i'"


def test_cpu_cache_level2():
    assert cpu.l2() == 524288

def test_cpu_cache_level3():
    assert cpu.l3() == 4194304
