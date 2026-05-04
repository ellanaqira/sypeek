import pytest
from sypeek import memory as mem


def test_total_memory():
    assert mem.mem_total() == 16053928

def test_free_memory():
    assert mem.mem_free()

def test_available_memory():
    assert mem.mem_available()
