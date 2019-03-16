from collections import Counter
class List(object):
    def count_spec_digits(self, integers_list, digits_list):
        c = Counter("".join([str(i) for i in integers_list]))
        return [(int(x) ,c[str(x)]) for x in digits_list]
