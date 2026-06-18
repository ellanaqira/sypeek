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
    


def get_cpudt_stc(keyword: str, core_num: int = 0):
    """
    Get static information for each logical core on cpu.
    cpudt_stc means CPU DaTa StaTiC, where all the data
    about the CPU that is taken is static data or data
    that does not change.

    Parameters:
    * keyword: str  = keyword to get related data from selected core (core_num: int)
    * flags (special keyword: str):
        * The core_num parameter is ignored, meaning the flags below
          will return output without regard to the number of cores.
            - "--all"   : return sorted list of data from each logical core
            - "--allraw"   : return all cpu core data in form of list[dict]

        * Depending on the core_num parameter, it means the flags below will
          return output based on the number from the core_number parameter.
            - "--sel" : return selected core data by the number of the core (core_num: int)
            - "--selraw"   : returns selected core (core_num: int) data in form of dictionary
            - "--len"   : returns the number of data from the selected core (core_num: int)
    * core_num: int = the number of the core whose data you want to get,
      the default value is 0
    """
    try:    
        data = subprocess.run(["cpuid"], capture_output=True, text=True)
    except FileNotFoundError:
        raise CPUInfoError("failed to get cpu data")
    else:    
        raw_cpu_data = data.stdout.splitlines()

        temp_core_data = [] # temporary store data per-core
        temp_cpu_list = [] # temporary store core data set from temp_core_data variable 
        i: int = 1
        for data in raw_cpu_data:
            if data == f"CPU {i}:":
                temp_core_data.sort()
                temp_cpu_list.append(temp_core_data)
                temp_core_data = []
                i = i+1
            temp_core_data.append(data)
        temp_core_data.sort()
        temp_cpu_list.append(temp_core_data)

        cpu_dict = {} # store data per-core in form of dictionary
        cpu_organize_data = [] # store organize cpu_dict data
        for temp_core_data in temp_cpu_list:
            for data in temp_core_data:
                try:
                    key, value = data.split("=", 1)
                except ValueError:
                    continue
                else:
                    key, value = key.strip(), value.strip().replace('"','')
                    cpu_dict[key] = value
            cpu_organize_data.append(cpu_dict)
            cpu_dict = {}

        try:
        # output that ignores the core_num value
            if keyword == "--all":
            # find longest key for formated and neater output
                longest_key :int = 0
                for cpu in cpu_organize_data:
                    for key in cpu.keys():
                        if len(key) > longest_key:
                            longest_key = len(key)
            
            # create formated data
                formated_output = []
                i :int = 0
                for cpu in cpu_organize_data:
                    formated_output.append(f"# CPU {i} :")
                    for key,value in cpu.items():
                        formated_output.append((f"{key}{" "*(longest_key-(len(key)))} : {value}"))
                    formated_output.append(f"[data length = {len(cpu)}]")
                    formated_output.append("\n")
                    i = i+1
                return _VerticalList(formated_output)

            if keyword == "--allraw":
                return cpu_organize_data
            

        # output that is affected by the core_num value
            if keyword == "--sel":
            # find longest key for formated and neater output
                longest_key :int = 0
                for cpu in cpu_organize_data:
                    for key in cpu.keys():
                        if len(key) > longest_key:
                            longest_key = len(key)

            # create formated data
                formated_output = []
                formated_output.append(f"# CPU {core_num} :")
                for key, value in cpu_organize_data[core_num].items():
                    formated_output.append((f"{key}{" "*(longest_key-(len(key)))} : {value}"))
                formated_output.append(f"[data length = {len(cpu_organize_data[core_num])}]")
                return _VerticalList(formated_output)
    
            if keyword == "--selraw":
                return cpu_organize_data[core_num]        

            if keyword == "--len":
                return len(cpu_organize_data[core_num])


        # return data by keyword and core_num
            return cpu_organize_data[core_num][keyword]
        
        except KeyError:
            raise CPUInfoError(f"the data of '{keyword}' not available")
        except IndexError:
            raise CPUInfoError(f"core number must be int() and between 0 and {len(cpu_organize_data)-1}")



def get_cpudt_dynmc(keyword: str, core_num: int = 0):
    """
    Get information for each logical core on cpu.
    cpudt_dynmc means CPU DaTa DYNaMiC, which means
    that the data about the CPU that is taken contains
    some dynamic or changing data and is not fixed.

    Parameters:
    * keyword: str  = keyword to get related data from selected core (core_num: int)
    * flags (special keyword: str):
        * The core_num parameter is ignored, meaning the flags below
          will return output without regard to the number of cores.
            - "--all"   : return sorted list of data from each logical core
            - "--raw"   : return all cpu core data in form of list[dict]

        * Depending on the core_num parameter, it means the flags below will
          return output based on the number from the core_number parameter.
            - "--sel" : return selected core data by the number of the core (core_num: int)
            - "--len"   : returns the number of data from the selected core (core_num: int)
    * core_num: int = the number of the core whose data you want to get,
      the default value is 0
    """

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
        raise CPUInfoError("failed to get cpu data")

    else:
        longest_key = 0
        for processor in cpu_list:
            for key in processor.keys():
                len_temp = len(key)
                if len_temp > longest_key:
                    longest_key = len_temp

        try:
        # output that ignores the core_num value
            if keyword == "--all":
                sorted_list = []
                for processor in cpu_list:
                    for key,value in processor.items():
                        sorted_list.append((f"{key}{" "*(longest_key-len(key))} : {value}"))
                    sorted_list.append(len(processor))
                    sorted_list.append("\n")
                
                return _VerticalList(sorted_list)
            
            if keyword == "--raw":
                return cpu_list
            

        # output that is affected by the core_num value
            if keyword == "--sel":
                sorted_list = []
                for key,value in cpu_list[core_num].items():
                    sorted_list.append((f"{key}{" "*(longest_key-len(key))} : {value}"))
                sorted_list.append(f"[data length = {len(cpu_list[core_num])}]")
                                    
                return _VerticalList(sorted_list)
                

            if keyword == "--len":
                return len(cpu_list[core_num])
                    
            
            return cpu_list[core_num][keyword]
        except KeyError:
            raise CPUInfoError(f"the data of '{keyword}' not available")
        except IndexError:
            raise CPUInfoError(f"core number must be int() and between 0 and {len(cpu_list)-1}")



def get_cpudt_snsr(keyword: str):
    """
    Snsr means SeNSoRs, get information about
    cpu from sensors by a keyword.
    
    Parameters:
    * keyword: str = keyword to get related data
    * flags (special keyword: str):
        - "--all" : return sorted list of data
        - "--raw" : return data in form of raw dictionary
        - "--len" : returns the number of data  
    """

    try:
        data = subprocess.run(["sensors"], capture_output=True, text=True)
    except FileNotFoundError:
        raise CPUInfoError("failed to get cpu data")
    else:
        raw_sensor_data = data.stdout.splitlines()
        sensor_dict = {}

        for data in raw_sensor_data:
            if ":" not in data:
                continue
            key, value = data.split(":")
            key, value = key.strip().replace('"',''), value.strip().replace('"','')
            sensor_dict[key] = value

        if keyword == "--all":
            longest_key = 0
            for key in sensor_dict.keys():
                if len(key) > longest_key:
                    longest_key = len(key)

            formated_sensor_data = []
            for key,value in sensor_dict.items():
                formated_sensor_data.append(f"{key}{" "*(longest_key-len(key))} : {value}")

            return _VerticalList(formated_sensor_data)
        
        if keyword == "--raw":
            return sensor_dict
        
        if keyword == "--len":
            return len(sensor_dict)
        
        try:
            return sensor_dict[keyword]
        except KeyError:
            raise CPUInfoError(f"the data of '{keyword}' not available")
    