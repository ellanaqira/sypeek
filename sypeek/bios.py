class BIOSInfoError(Exception):
    """
    Exception raised and displays an error message
    when a problem occurs while trying to retrieve
    bios information.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


def _get_bios_info(file_name: str, keyword_error: str):
    try:
        with open(f"/sys/class/dmi/id/{file_name}") as f:
            return (f.read().strip())

    except FileNotFoundError:
        raise BIOSInfoError(f"Couldn't get '{keyword_error}' information")
    

def bios_vendor():
    return _get_bios_info("bios_venor", "BIOS Vendor")

def bios_date():
    return _get_bios_info("bios_date", "BIOS Date")

def bios_version():
    return _get_bios_info("bios_release", "BIOS Version")
