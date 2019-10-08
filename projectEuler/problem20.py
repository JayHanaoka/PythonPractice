def factSum(n):
    strFact = str(fact(n))
    total = 0
    
    for c in strFact:
        total += int(c)
    return total

def fact(n):
    fact = 1
    
    if n < 0:
        return 0
    elif n == 0:
        return fact
    else:
        for i in range(1, n+1):
            fact = fact * i
    return fact
    
print(factSum(100))