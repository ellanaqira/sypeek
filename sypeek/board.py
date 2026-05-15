
class _Get_Board_Info:
    def __init__(self, file_name: str, keyword_error: str):
        self.file_name = file_name
        self.keyw_error = keyword_error

    def _get_board_info(self):
        try:
            with open(f"/sys/class/dmi/id/{self.file_name}") as f:
                return (f.read().strip())

        except FileNotFoundError:
            return f"Couldn't get '{self.keyw_error}' information"


def board_name():
    return _Get_Board_Info("board_name", "Board Name")._get_board_info()

def board_vendor():
    return _Get_Board_Info("board_vendor", "Board Vendor")._get_board_info()

def board_version():
    return _Get_Board_Info("board_version", "Board Version")._get_board_info()
