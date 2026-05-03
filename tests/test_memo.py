import pytest
from sypeek import memory as mem


# Memory Test ===============================

def test_total_memory():
    assert mem.mem_total() == 16053928

def test_used_memory():
    assert mem.mem_used()

def test_free_memory():
    assert mem.mem_free()

def test_available_memory():
    assert mem.mem_available()


# Memory Swap Test ==========================

def test_total_swap_memory():
    assert mem.swap_mem_total() == 2097148

def test_used_swap_memory():
    assert mem.swap_mem_used() == 0

def test_free_swap_memory():
    assert mem.swap_mem_free() == 2097148