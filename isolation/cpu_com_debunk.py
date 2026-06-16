import subprocess


class CPUInfoError(Exception):
    """
    Exception raised and displays an error message
    when a problem occurs while trying to retrieve
    cpu information.

    Attributes:
    * message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class _VerticalList:
    """
    Return "vertical list" from the raw list.

    Atributes:
    * data_list = raw list that want to turn into "vertical list"
    """
    def __init__(self, data_list: list[str]):
        self.data_list = data_list

    def __str__(self):
        string_list = []
        for data in self.data_list:
            string_list.append(str(data))

        return "\n".join(string_list)
    

# static data (doesnt change)
def get_cpudt_gnrl(keyword: str):
    """
    Gnrl means GeNeRaL, get general
    information about cpu by a keyword.
    
    Parameters:
    * keyword: str = keyword to get related data
    * flags (special keyword: str):
        - "--all" : return sorted list of data
        - "--raw" : return data in form of raw dictionary
        - "--len" : returns the value of the amount of data  
    """
    try:
        data = subprocess.run(["cpuid"], capture_output=True, text=True)

    except FileNotFoundError:
        raise CPUInfoError("failed to get cpu data")
    
    else:
        raw_cpu_data = data.stdout.splitlines()
        cpu_dict = {}
        cpu_list = []
        cpu_list_sorted = []

    # store data into cpu_dict variable
        for data in raw_cpu_data:
            if ":" in data or "-" in data:
                continue
            key, value = data.split("=")
            key, value = key.strip().replace('"',''), value.strip().replace('"','')
            cpu_dict[key] = value
        
    # store unsorted data into cpu_list variable
        # get the longest key from cpu_dict variable
        # to align the number of spaces
        longest_key = 0
        for key in cpu_dict.keys():
            len_temp = len(key)
            if len_temp > longest_key:
                longest_key = len_temp

        for key,value in cpu_dict.items():
            cpu_list.append(f"{key}{' '*(longest_key-len(key))} : {value}")
        cpu_list.sort()

        try:
            if keyword == "--all":        
                return _VerticalList(cpu_list)
            
            elif keyword == "--raw":
                return cpu_dict

            elif keyword == "--len":
                return len(cpu_list)
            
            else:
                return cpu_dict[keyword]
        except KeyError:
            raise CPUInfoError(f"the data of '{keyword}' not available")
        


def get_cpudt_pcr(keyword: str, core_num: int = 0):
    """
    Pcr means Per-CoRe, get information
    for each logical core on cpu.

    Parameters:
    * keyword: str  = keyword to get related data from selected core (core_num: int)
    * flags (special keyword: str):
        * The core_num parameter is ignored, meaning the flags below
          will return output without regard to the number of cores.
            - "--all"   : return sorted list of data from each logical core
            - "--raw"   : return all cpu core data in form of list[dict]

        * Depending on the core_num parameter, it means the flags below will
          return output based on the number from the core_number parameter.
            - "--ncore" : return selected core data by the number of the core (core_num: int)
            - "--len"   : returns the number of data from the selected core (core_num: int)
    * core_num: int = the number of the core whose data you want to get,
      the default value is 0
    """
     # function to retrive information from cpuinfo file
    cpu_list = []
    try:
        with open("/proc/cpuinfo") as f:
            cpu_dict = {}
            for line in f:
                line = line.strip()

                if not line:
                    if cpu_dict:
                        cpu_list.append(cpu_dict)
                        cpu_dict = {}
                    continue
                key, value = [x.strip() for x in line.split(":", 1)]
                cpu_dict[key] = value

            # store the last cpu information, because there is no empty line at the end of the file  
            if cpu_dict:
                cpu_list.append(cpu_dict)

    except FileNotFoundError:
        raise "Error"

    else:
        longest_key = 0
        for processor in cpu_list:
            for key in processor.keys():
                len_temp = len(key)
                if len_temp > longest_key:
                    longest_key = len_temp

        if keyword == "--all":
            sorted_list = []
            for processor in cpu_list:
                for key,value in processor.items():
                    sorted_list.append((f"{key}{" "*(longest_key-len(key))} : {value}"))
                sorted_list.append("\n")
            
            return _VerticalList(sorted_list)
        
        if keyword == "--raw":
            return cpu_list
        
        
        if keyword == "--ncore":
            sorted_list = []
            try:
                for key,value in cpu_list[core_num].items():
                    sorted_list.append((f"{key}{" "*(longest_key-len(key))} : {value}"))
            except IndexError:
                raise CPUInfoError(f"core number must be int() and between 0 and {len(cpu_list)-1}")
            else:
                return _VerticalList(sorted_list)
            

        if keyword == "--len":
            try:
                return len(cpu_list[core_num])
            except IndexError:
                raise CPUInfoError(f"core number must be int() and between 0 and {len(cpu_list)-1}")
                
        try:
            return cpu_list[core_num][keyword]
        except KeyError:
            raise CPUInfoError(f"the data of '{keyword}' not available")
        except IndexError:
            raise CPUInfoError(f"core number must be int() and between 0 and {len(cpu_list)-1}")
            
