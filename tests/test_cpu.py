from sypeek import cpu
import pytest

def test_cpu_vendor():
    assert cpu.vendor() == "AMD"

def test_cpu_vendorid():
    assert cpu.vendorid() == "AuthenticAMD"

def test_cpu_name():
    assert cpu.name() == "AMD Ryzen 5 3500U with Radeon Vega Mobile Gfx"

def test_cpu_threads():
    assert cpu.threads() == 2

def test_cpu_cores():
    assert cpu.cores('l') == 8 # logical core(s)
    assert cpu.cores('p') == 4 # physical core(s)
    assert cpu.cores('L') == 8 # logical core(s)
    assert cpu.cores('P') == 4 # physical core(s)

    with pytest.raises(ValueError, match="core must be 'l' or 'p'"):
        cpu.cores('q')

def test_cpu_family():
    assert cpu.family() == "0xf (15)"

def test_cpu_family_synth():
    assert cpu.family_synth() == "0x17 (23)"

def test_cpu_model():
    assert cpu.model() == "0x8 (8)"

def test_cpu_model_synth():
    assert cpu.model_synth() == "0x18 (24)"

def test_cpu_stepping():
    assert cpu.stepping() == 1
