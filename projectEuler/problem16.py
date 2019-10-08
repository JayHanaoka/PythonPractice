def sumPower(n):
    num = str(2**n)
    
    return sumUp(num)
def sumUp(s):
    result = 0
    for i in range(0, len(s)):
        result += int(s[i])
    return result
    
print(sumPower(1000))