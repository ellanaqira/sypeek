# Sypeek
Python library for monitor CPU, Memory, Motherboard, Operating System, and BIOS in Linux. 

### - Note:
<mark> This library is intended for Ubuntu-based Linux distributions.</mark> For other Linux-based distributions, it cannot be guaranteed that it will work properly.

## Usage
```python
from sypeek import cpu, memory

# return cpu name and cpu temperature in celcius
print(f"=====(CPU info)=====")
print(f"name : {cpu.cpu_model_name()}")
print(f"temp : {cpu.cpu_temp('c')} °C")

# return total memory and used memory
print("=====(Memo info)=====")
print(f"total: {memory.mem_total()}")
print(f"used : {memory.mem_used()}")
``` 
output:

```
=====(CPU info)=====
name : Intel Core i5 7200u
temp : 44.8 °C
=====(Memo info)=====
total: 16053936 
used : 5592892
```

## Status
Work in progress... 🚧🛠️


## Contributing
This project is still a work in progress, and contributions are highly appreciated`:D`.
Feel free to fork, improve, or suggest ideas. Don't hesitate to open issues or pull requests.