cases = int(input())

for i in range(cases):
    size = int(input())
    nums = list(map(int, input().split()))
    for i in range(size):
        if nums[i] != i+1:
            print(i+1)
            break
    