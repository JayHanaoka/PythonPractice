import math

def smallestMultiple(n):
    m = 1 
    for i in range(1, n+1):
        m = m * i // math.gcd(m, i)
    print(m)
    
smallestMultiple(20)