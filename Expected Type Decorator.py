class UnexpectedTypeException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return "{} is not expected return type".format(self.value)

def expected_type(return_types):
    def Wrapper(f):
        def inner(*args):
            result = f(*args)
            res = False
            for exp_type in return_types:
                if isinstance(result, exp_type):
                    return result
            raise UnexpectedTypeException(type(result))
        return inner
    return Wrapper