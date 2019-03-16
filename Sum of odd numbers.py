def row_sum_odd_numbers(n):
    k=0
    i=n
    while i>0:
        k=k+i
        i=i-1    
    an = 1+(k-1)*2    
    sum=0
    i=n
    while i>0:
        sum=sum+an
        an=an-2
        i=i-1
    return sum
