class value(int): pass
def nt(self, a, b):
    self.a = a
    self.b = b   
import operator as o
for s in ['add','sub','mul','truediv','mod','pow']:
    vars()[s] = type(s, (), {"__init__": nt, "compute": lambda self: self.g(self.a, self.b), "g":getattr(o, s)})

