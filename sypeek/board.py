import os

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


class _VerticalList:
    """
    Return "vertical list" from the raw list.

    Atributes:
    * data_list = raw list that want to turn into "vertical list"
    """
    def __init__(self, data_list):
        self.data_list = data_list


    def __str__(self):
        longest_key: int = 0
        for data in self.data_list:
            for key in data.keys():
                if len(key) > longest_key:
                    longest_key = len(key)

        organize = []
        for data in self.data_list:
            for key,value in data.items():
                organize.append(f"{key}{" "*(longest_key-len(key))} : {value}")
            organize.append("\n")

        return "\n".join(organize)



def get_brddt(keyword: str):
    """
    brddt means BoaRD DaTa, this funtion is used to
    get information about board by a keyword.
    
    Parameters:
    * keyword: str = keyword to get related data
    * flags (special keyword: str):
        - "--all" : return sorted list of data
        - "--raw" : return data in form of raw dictionary
        - "--len" : returns the number of data  
    """
    board_data = {}
    p: str = "/sys/class/dmi/id/"
    try:
        for plnf in os.scandir(p):
            if plnf.is_file():
                try:
                    with open(plnf.path, "r") as f:
                        board_data[os.path.basename(plnf)] = (f.read()).strip()
                except PermissionError:
                    None 
        try:
            if keyword == "--all":
                return _VerticalList([board_data])
            
            if keyword == "--raw":
                return board_data
            
            if keyword == "--len":
                return int(len(board_data))

            return board_data[keyword]
        except KeyError:
            raise BoardInfoError(f"the data of '{keyword}' not available")
        
    except FileNotFoundError:
        raise BoardInfoError("failed to get board data")
    