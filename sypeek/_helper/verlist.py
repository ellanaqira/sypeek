class _VerticalList:
    """
    Return "vertical list" from the raw list.

    Atributes:
    * data_list = raw list that want to turn into "vertical list"
    """
    def __init__(self, data_list: list):
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
