import subprocess
from _verlist import _VerticalList as _VerList


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
    


def get_cpudt_sttc(keyword: str, core_num: int = 0):
    """
    Get static information for each logical core on cpu.
    cpudt_sttc means CPU DaTa STaTiC, where all the data
    about the CPU that is taken is static data or data
    that does not change.

    Parameters:
    * keyword: str  = keyword to get related data from selected core (core_num: int)
    * flags (special keyword: str):
        * The core_num parameter is ignored, meaning the flags below
          will return output without regard to the number of cores.
            - "--all"   : return sorted list of data from each logical core
            - "--allraw"   : return all cpu core data in form of list[dict]
            - "--allen"   : returns the length of entire data

            
        * Depending on the core_num parameter, it means the flags below will
          return output based on the number from the core_number parameter.
            - "--sel"     : return selected core data by the number of the core (core_num: int)
            - "--selraw"  : return selected core (core_num: int) data in form of dictionary
            - "--sellen"  : return the length of selected core data (core_num: int)
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
                return _VerList(cpu_organize_data)

            if keyword == "--allraw":
                return cpu_organize_data
            
            if keyword == "--allen":
                return int(len(cpu_organize_data) * len(cpu_organize_data[core_num]))

        # output that is affected by the core_num value
            if keyword == "--sel":
                return _VerList([cpu_organize_data[core_num]])
    
            if keyword == "--selraw":
                return cpu_organize_data[core_num]        

            if keyword == "--sellen":
                return len(cpu_organize_data[core_num])


        # return data by keyword and core_num
            return cpu_organize_data[core_num][keyword]
        
        except KeyError:
            raise CPUInfoError(f"the data of '{keyword}' not available")
        except IndexError:
            raise CPUInfoError(f"core number must be int() and between 0 and {len(cpu_organize_data)-1}")
        except TypeError:
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
            - "--all"    : return sorted list of data from each logical core
            - "--allraw" : return all cpu core data in form of list[dict]
            - "--allen"  : returns the length of entire data

            
        * Depending on the core_num parameter, it means the flags below will
          return output based on the number from the core_number parameter.
            - "--sel"    : return selected core data by the number of the core (core_num: int)
            - "--selraw" : return selected core (core_num: int) data in form of dictionary
            - "--sellen" : return the length of selected core data (core_num: int)
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
        try:
        # output that ignores the core_num value
            if keyword == "--all":
                return _VerList(cpu_list)
            
            if keyword == "--allraw":
                return cpu_list
            
            if keyword == "--allen":
                return int(len(cpu_list) * len(cpu_list[core_num]))

        # output that is affected by the core_num value
            if keyword == "--sel":  
                return _VerList([cpu_list[core_num]])
            
            if keyword == "--selraw":
                return cpu_list[core_num]

            if keyword == "--sellen":
                return int((len(cpu_list[core_num])))
                    
            
            return cpu_list[core_num][keyword]
        except KeyError:
            raise CPUInfoError(f"the data of '{keyword}' not available")
        except IndexError:
            raise CPUInfoError(f"core number must be int() and between 0 and {len(cpu_list)-1}")
        except TypeError:
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
            formated = [sensor_dict]
            return _VerList(formated)
        
        if keyword == "--raw":
            return sensor_dict
        
        if keyword == "--len":
            return int(len(sensor_dict))
        
        try:
            return sensor_dict[keyword]
        except KeyError:
            raise CPUInfoError(f"the data of '{keyword}' not available")
        