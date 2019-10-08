def fib():
    num = 1000
    first = 0
    second = 1
    fibList = [first, second]
    result = 0
    
    for i in range(2, num):
        temp = fibList[i-2] + fibList[i-1]
        fibList.append(temp)
        if temp % 2 == 0 and temp <= 4000000:
            result += temp

    print(result)
     
fib()