
def _get_board_info(file_name: str, keyword_error: str):
    try:
        with open(f"/sys/class/dmi/id/{file_name}") as f:
            return (f.read().strip())

    except FileNotFoundError:
        return f"Couldn't get '{keyword_error}' information"
    

def board_name():
    return _get_board_info("board_name", "Board Name")

def board_vendor():
    return _get_board_info("board_vendor", "Board Vendor")

def board_version():
    return _get_board_info("board_version", "Board Version")
