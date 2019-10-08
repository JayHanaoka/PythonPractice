cases = int(input())

for i in range(cases):
    size, total = map(int, input().split())
    nums = list(map(int, input().split()))
    found = False
    
    for i in range(size):
        for j in range(i+1, size):
            if nums[i] + nums[j] == total:
                print("Yes")
                found = True
                break
    if not found:
        print("No")