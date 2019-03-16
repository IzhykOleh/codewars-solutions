def zero(oper=0): return 0 if oper==0 else oper(0)
def one(oper=1): return 1 if oper==1 else oper(1)
def two(oper=2): return 2 if oper==2 else oper(2)
def three(oper=3): return 3 if oper==3 else oper(3)
def four(oper=4): return 4 if oper==4 else oper(4)
def five(oper=5): return 5 if oper==5 else oper(5)
def six(oper=6): return 6 if oper==6 else oper(6)
def seven(oper=7): return 7 if oper==7 else oper(7)
def eight(oper=8): return 8 if oper==8 else oper(8)
def nine(oper=9): return 9 if oper==9 else oper(9)
def ten(oper=10): return 10 if oper==10 else oper(10)

def times(num): return lambda a : a*num
def plus(num): return lambda a:a+num
def minus(num): return lambda a:a-num
def divided_by(num): return lambda a:a//num
