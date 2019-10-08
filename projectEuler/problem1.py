def sumMultiples():
    result = 0
    num = 1000
    for i in range(0, num):
        if (i % 3 == 0 or i % 5 == 0):
            result += i
    print(result)
    
sumMultiples()