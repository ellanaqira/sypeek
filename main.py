import subprocess

def proc_name():
    # return processor name
    cmd = "lscpu | grep 'Model name'"
    raw_proc_name = subprocess.run(cmd, capture_output=True, text=True, shell=True).stdout
    proc_name = raw_proc_name.split(":")[1].strip()
    return proc_name