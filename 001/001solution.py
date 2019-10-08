cases = int(input())

for i in range(cases):
    
    size, total = map(int, input().split())
    nums = list(map(int,input().split()))
    found = False

    start = 0
    while start < size:
        for i in range(start, size):
            if sum(nums[start:i]) == total:
                print(str(start+1) + ' ' + str(i))
                found = True
                break
        if not found:
            start += 1
            continue
        break
    if not found:
        print(-1)
            
    