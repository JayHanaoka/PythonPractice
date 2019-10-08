import math

def runDiff(n):
    return sqSum(n) - sumSq(n)

def sumSq(n):
    result = 0
    for i in range(1, n+1):
        result += i ** 2
    return result

def sqSum(n):
    result = 0
    for i in range(1, n+1):
        result += i
    return result ** 2

print(runDiff(100))