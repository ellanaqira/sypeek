from sypeek import *

# return cpu name and cpu temperature in celcius
print(f"=====(CPU info)=====")
print(f"name : {cpu.name()}")
print(f"temp : {cpu.temp()} °C")

# return total memory and used memory
print("=====(Memo info)=====")
print(f"total: {memory.total()}")
print(f"used : {memory.used()}")