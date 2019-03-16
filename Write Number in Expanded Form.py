def expanded_form(num):
    l=[]
    length=len(str(num))
    ros=length
    dif=0
    while ros>0:
        dif=10**(length-ros)
        if num%10 != 0:
            l.append(int(num%10*dif))
            num=num//10
        else:           
            num=num/10        
        ros=ros-1
    l.reverse()
    l = list(map(lambda x: str(x), l))
    return ' + '.join(l)
