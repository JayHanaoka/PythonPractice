# cook your dish here
import math

def pal(first):
    second = first
    maxPal = 0
    
    for i in reversed(range(first)):
        for j in reversed(range(second)):
            result = i * j
            if checkPal(result) and result > maxPal:
                maxPal = result
                print(result)

def checkPal(n):
    n = str(n)
    m = n[::-1]
    l = len(n)/2
    
    if l % 2 == 0:
        return n[0:int(l)] == m[0:int(l)]
    l += .5
    return m[0:int(l)] == n[0:int(l)]
    
pal(1000)