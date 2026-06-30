from ._verlist import _VerticalList as _VerList


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


class _ReadSF:
    """
    Read file and return it as a string.

    Attributes:
    * file_path -- the relative file path of destination file in string
    """
    def __init__(self, file_path: str):
        self.fpath = file_path

    def returnstr(self):
        try:
            with open(self.fpath) as f:
                result = f.read()
        except FileNotFoundError:
            return "failed to get operating system data (!)" 
        else:
            return result.strip()
    

def get_osdt(keyword: str):
    """
    Osdt means Operating System DaTa, get information about
    operating system by a keyword.
    
    Parameters:
    * keyword: str = keyword to get related data
    * flags (special keyword: str):
        - "--all" : return sorted list of data
        - "--raw" : return data in form of raw dictionary
        - "--len" : returns the number of data  
    """
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

        ver = _ReadSF("/proc/version")
        os_info_dict["FULL_VERSION"] = ver.returnstr()

        ver_sig = _ReadSF("/proc/version_signature")
        os_info_dict["VERSION_SIGNATURE"] = ver_sig.returnstr()

        host_name = _ReadSF("/etc/hostname")
        os_info_dict["HOST_NAME"] = host_name.returnstr()

        try:
            if keyword == "--all":
                return _VerList([os_info_dict])
            if keyword == "--raw":
                return os_info_dict
            if keyword == "--len":
                return len(os_info_dict)
            
            return os_info_dict[keyword]
        
        except KeyError:
            raise OpSyInfoError(f"the data of '{keyword}' not available")

    except FileNotFoundError:
        raise OpSyInfoError("failed to get operating system data (!)")



def get_uptime(appearance: str = ""):
    """
    Returns the value of how long the device was active,
    at default this function return in minutes.

    Parameter:  
    * appearance: str
        you can leave it blank or insert "p"/"P" to
        return the time value in "pretty" or human
        readable format
    """

    try:
        with open("/proc/uptime") as time:
            time = time.read().split()
            time =int(float(time[0]) / 60)
            
    except FileNotFoundError:
        raise OpSyInfoError(f"the data of 'Uptime' not available")

    else:
        if appearance.lower() == 'p':
            # return uptime in 'pretty' format
            hour: int = 0
            if time >= 60:
                while time >= 60:
                    time = time-60
                    hour = hour + 1

            minutes = time
            return f"{hour} hours, {minutes} minutes"            
            
        elif appearance == "":
            # return uptime in minutes
            return int(time)
        
        else:
            return "appearances most be 'p' or an empty string"  