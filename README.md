# Sypeek
Python library for monitor CPU, Memory, Motherboard, Operating System, and BIOS in Linux.

This Python library is very simple and easy to use, all you need to do to get information about CPU, Memory, Motherboard, Operating System, and BIOS is just call a function, and some other functions require you to add arguments. 

### - Note:
<mark> This library is intended for Ubuntu-based Linux distributions.</mark> For other Linux-based distributions, it cannot be guaranteed that it will work properly.

## Documentation

### ___ Bios ___________________________________________________
`from sypek.bios import *` will give you available function inside of bios module that you can use to get information about your bios.

`bios_vendor()` - return the vendor name of bios <br>
`bios_date()` - return the date of the bios in "pretty" format <br>
`bios_version()` - return the version of bios on your machine


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