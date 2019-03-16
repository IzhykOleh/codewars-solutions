def common_mul(a,b):
	if a%b == 0:
		return a
	if b%a == 0:
		return b
	return a*b
    
def common_div(a,b):
    li_a, li_b = [], []
    for x in range(2, a+1):
        if a%x==0:
            li_a+=[x]
    for y in range(2, b+1):
        if b%y==0:
            li_b+=[y]
    try:
        return max(set(li_a).intersection(set(li_b)))
    except ValueError:
        return 0

class Fraction:

    def __init__(self, numerator, denominator):
        self.top = numerator
        self.bottom = denominator
    
    #Equality test
    
    def __eq__(self, other):
        first_num = self.top * other.bottom
        second_num = other.top * self.bottom
        return first_num == second_num
        
    def __add__(self, other):
        new_bottom = common_mul(self.bottom, other.bottom)
        new_top = new_bottom/self.bottom * self.top + new_bottom/other.bottom * other.top
        cd = common_div(new_top, new_bottom)
        if cd!=0:
            new_top/=cd
            new_bottom/=cd
        return Fraction(new_top, new_bottom)
        
    def __str__(self):
        return '%i/%i' % (self.top, self.bottom)
