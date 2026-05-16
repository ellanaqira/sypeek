class OpSyInfoError(Exception):
    """
    Exception raised and displays an error message
    when a problem occurs while trying to retrieve
    operating system information.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


def _raise_opsyinfoerror(keyword_error: str):
    raise OpSyInfoError(f"Couldn't get '{keyword_error}' information")


def _get_os_info(keyword: str, keyword_error: str):
    error_msg: str = f"Couldn't get '{keyword_error}' information"

    os_info_list: list = []
    os_info_dict: dict = {}

    try:
        with open(f"/etc/os-release") as f:
            f = f.read().strip().split('\n')

        for line in f:
            line = line.split('=')
            os_info_list.append(line)

        for data in os_info_list:
            key = data[0]
            value = str(data[1]).replace('"', '')
            os_info_dict[key] = value

        try:
            return os_info_dict[keyword]
        except KeyError:
            raise OpSyInfoError(error_msg)

    except FileNotFoundError:
        raise OpSyInfoError(error_msg)
    


def opsy_kernel():
    try:
        with open("/proc/version") as f:
            f = f.read().split('(')
    except FileNotFoundError:
        _raise_opsyinfoerror("Kernel Name")   
    else:
        return f[0].strip()
    
def hosts_name():
    try:
        with open("/etc/hostname") as f:
            f = f.read().strip()
    except FileNotFoundError:
        _raise_opsyinfoerror("Host Name")
    else:
        return f
    
def distro_name():
    return _get_os_info("NAME", "Distribution Name")

def distro_ver():
    return _get_os_info("VERSION_ID", "Distribution Version")

def uptime(option: str = ""):
    try:
        with open("/proc/uptime") as time:
            time = time.read().split()
            time =int(float(time[0]) / 60)
            
    except FileNotFoundError:
        _raise_opsyinfoerror("Uptime")

    else:
        if option.lower() == 'p':
            # return uptime in 'pretty' format
            hour: int = 0
            if time >= 60:
                while time >= 60:
                    time = time-60
                    hour = hour + 1

            minutes = time
            return f"{hour} hours, {minutes} minutes"            
            
        elif option == "":
            # return uptime in minutes
            return int(time)
        
        else:
            return "options most be 'p' or an empty string"