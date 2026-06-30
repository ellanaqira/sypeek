from sypeek import board
from sypeek import cpu
from sypeek import memory
from sypeek import opsy


# BOARD INFORMATION
def get_board_info():
    print("    _____________ ")
    print("<> |____BOARD____|\n")
    print("* Keyword = '--all'")
    print(board.get_brddt("--all"))

    print("* Keyword = '--raw'")
    print(board.get_brddt("--raw"))

    print("\n\n* Keyword = '--len'")
    print(board.get_brddt("--len"))

    print("\n\n* Keyword = 'product_name'")
    print(board.get_brddt("product_name"))


# CPU INFORMATION    
def _get_all_cpu_static_info():
    print("* Keyword = '--all'")
    print(cpu.get_cpudt_sttc("--all"))

    print("* Keyword = '--allraw'")
    print(cpu.get_cpudt_sttc("--allraw"))

    print("\n\n* Keyword = '--allen'")
    print(cpu.get_cpudt_sttc("--allen"))

def _get_selected_cpu_static_info():
    print("* Keyword = '--sel', core_num = 1")
    print(cpu.get_cpudt_sttc("--sel", 1))

    print("* Keyword = '--selraw', core_num = 1")
    print(cpu.get_cpudt_sttc("--selraw", 1))

    print("\n\n* Keyword = '--sellen', core_num = 1")
    print(cpu.get_cpudt_sttc("--sellen", 1))

def _get_all_cpu_dynamic_info():
    print("* Keyword = '--all'")
    print(cpu.get_cpudt_dynmc("--all"))

    print("* Keyword = '--allraw'")
    print(cpu.get_cpudt_dynmc("--allraw"))

    print("\n\n* Keyword = '--allen'")
    print(cpu.get_cpudt_dynmc("--allen"))

def _get_selected_cpu_dynamic_info():
    print("* Keyword = '--sel', core_num = 1")
    print(cpu.get_cpudt_dynmc("--sel", 1))

    print("* Keyword = '--selraw', core_num = 1")
    print(cpu.get_cpudt_dynmc("--selraw", 1))

    print("\n\n* Keyword = '--sellen', core_num = 1")
    print(cpu.get_cpudt_dynmc("--sellen", 1))

def _get_cpu_sensor_info():
    print("* Keyword = '--all'")
    print(cpu.get_cpudt_snsr("--all"))

    print("* Keyword = '--raw'")
    print(cpu.get_cpudt_snsr("--raw"))

    print("\n\n* Keyword = '--len'")
    print(cpu.get_cpudt_snsr("--len"))

    print("\n\n* Keyword = 'Tctl'")
    print(cpu.get_cpudt_snsr("Tctl"))


def get_cpu_info():
    print("\n")
    print("    _____________ ")
    print("<> |_____CPU ____|\n")
    _get_all_cpu_static_info()
    _get_selected_cpu_static_info()
    _get_all_cpu_dynamic_info()
    _get_selected_cpu_dynamic_info()
    _get_cpu_sensor_info()

    
# MEMORY INFORMATION
def get_memory_info():
    print("\n")
    print("    _____________ ")
    print("<> |____MEMORY___|\n")
    print("* Keyword = '--all'")
    print(memory.get_memdt("--all"))

    print("* Keyword = '--raw'")
    print(memory.get_memdt("--raw"))

    print("\n\n* Keyword = '--len'")
    print(memory.get_memdt("--len"))

    print("\n\n* Keyword = 'MemFree'")
    print(memory.get_memdt("MemFree"))

    
# OS INFORMATION
def get_opsy_info():
    print("\n")
    print("    _____________ ")
    print("<> |______OS_____|\n")
    print("* Keyword = '--all'")
    print(opsy.get_osdt("--all"))

    print("* Keyword = '--raw'")
    print(opsy.get_osdt("--raw"))

    print("\n\n* Keyword = '--len'")
    print(opsy.get_osdt("--len"))

    print("\n\n* Keyword = 'FULL_VERSION'")
    print(opsy.get_osdt("FULL_VERSION"))

    print("\n\n* Uptime")
    print(f"  '--- in minutes = {opsy.get_uptime()}")
    print(f"  '--- in pretty format = {opsy.get_uptime('p')}")


if __name__ == "__main__":
    get_board_info()
    get_cpu_info()
    get_memory_info()
    get_opsy_info()