class List(object):
    def remove_(self, integer_list, values_list):
        int_list = integer_list[:]
        for x in values_list:
            if x in integer_list:
                try:
                    while True:
                        int_list.remove(x)
                except ValueError:
                    pass
        return int_list
