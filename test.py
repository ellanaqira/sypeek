from sypeek import *

print("===[CPU Info]===")
print(cpu.name())
print(cpu.vendor())
print(cpu.temp())

print("===[MEMO Info]===")
print(memory.total())
print(memory.used())