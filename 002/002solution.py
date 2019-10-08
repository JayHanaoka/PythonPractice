cases = int(input())

for i in range(cases):
    size = int(input())
    nums = list(map(int, input().split()))
    
    if size%2 == 1:
        print(nums[int(size/2)])
    else:
        print(nums[int(size/2)])