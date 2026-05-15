class BoardInfoError(Exception):
    """
    Exception raised and displays an error message
    when a problem occurs while trying to retrieve
    motherboard information.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


def _get_board_info(file_name: str, keyword_error: str):
    try:
        with open(f"/sys/class/dmi/id/{file_name}") as f:
            return (f.read().strip())

    except FileNotFoundError:
        raise BoardInfoError(f"Couldn't get '{keyword_error}' information")
    

def board_name():
    return _get_board_info("board_name", "Board Name")

def board_vendor():
    return _get_board_info("board_vendor", "Board Vendor")

def board_version():
    return _get_board_info("board_version", "Board Version")
