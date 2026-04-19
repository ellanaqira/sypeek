# Sypeek
Simple system monitor library made in python for Linux. 

- Note:
For now, this library <mark>will likely only work smoothly and properly on Linux Mint or Ubuntu</mark>. In the future, I'll try to make it work on all Linux distributions.

## Usage
```python
from sypeek import *

# return cpu name and cpu temperature in celcius
print(f"=====(CPU info)=====")
print(f"name : {cpu.name()}")
print(f"temp : {cpu.temp()} °C")

# return total memory and used memory
print("=====(Memo info)=====")
print(f"total: {memory.total()} GB")
print(f"used : {memory.used()} GB")
``` 
output:
```
=====(CPU info)=====
name : Intel Core i5 7200u
temp : 44.8 °C
=====(Memo info)=====
total: 16.05 GB
used : 4.68 GB
```

## Status
Work in progress... 🚧🛠️

## Contributing
This project is still a work in progress, and contributions are highly appreciated`:D`.
Feel free to fork, improve, or suggest ideas. Don't hesitate to open issues or pull requests.