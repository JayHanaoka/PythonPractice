cases = int(input())

for i in range(cases):
    size = int(input())
    nums = list(map(int, input().split()))
    
    maxSum = min(nums)

    for i in range(0, size+1):
        for j in range(i+1, size+1):
            if sum(nums[i:j]) > maxSum:
                maxSum = sum(nums[i:j])

    print(maxSum)