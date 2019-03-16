class ABC:
    def __init__(self, string):
        self.values = [ch for ch in string]
        self.iter = iter(self)
    def __call__(self):
        return next(self.iter)
    def __iter__(self):
        self.n = 0
        return self
    def __next__(self):
        if self.n < len(self.values):
            self.n += 1
            return self.values[self.n-1]
        else:
            self.iter = iter(self)
            return next(self)

def make_looper(string):
    return ABC(string)
