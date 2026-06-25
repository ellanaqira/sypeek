class MemoInfoError(Exception):
    """
    Exception raised and displays an error message
    when a problem occurs while trying to retrieve
    memory information.

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
    def __init__(self, data_dict: dict[str]):
        self.data_dict = data_dict


    def __str__(self):
        longest_key: int = 0
        for key in self.data_dict.keys():
            if len(key) > longest_key:
                longest_key = len(key)

        organize = []
        for key,value in self.data_dict.items():
            organize.append(f"{key}{" "*(longest_key-len(key))} : {value}")

        return "\n".join(organize)
    


def get_memdt(keyword: str):
    """
    memdt means MEMory DaTa, get information about
    memory by a keyword.
    
    Parameters:
    * keyword: str = keyword to get related data
    * flags (special keyword: str):
        - "--all" : return sorted list of data
        - "--raw" : return data in form of raw dictionary
        - "--len" : returns the number of data  
    """
    data_dict = {}
    try:
        with open("/proc/meminfo") as f:
            for line in f:
                key, value = [x.strip().replace("kB", '').replace("kb", '') for x in line.split(':', 1)]
                data_dict[key] = value.strip()
                
    except FileNotFoundError:
        raise MemoInfoError("failed to get cpu data")
    
    else:
        # return value in bytes
        try:
            if keyword == "--raw":
                return data_dict
            
            if keyword == "--all":
                return _VerticalList(data_dict)
            
            if keyword == "--len":
                return int(len(data_dict))
            
            return int(data_dict[keyword])
        
        except KeyError:
            raise MemoInfoError(f"the data of '{keyword}' not available")
        