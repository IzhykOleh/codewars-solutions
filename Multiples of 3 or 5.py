def solution(num):
    g = lambda n: num//n-1 if num%n==0 else num//n
    fifteens = num//15
    
    def f(n, k): 
        counter=0
        li=[]
        for i in range(n):
            counter+=k
            li.append(counter)
        return sum(li)
    
    suma = f(g(3),3) + f(g(5),5)
    for i in range(fifteens):
        suma-=(i+1)*15
    return suma
        
