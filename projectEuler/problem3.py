# cook your dish here
import math

def lpf(n):
    
    for i in range(2, math.floor(math.sqrt(n))+1):
        if n % i == 0 and n / i != 1:
            n = n / i
            i = 1 
    
    print(n)
    return n

lpf(600851475143)