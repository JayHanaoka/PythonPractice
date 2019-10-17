def num_ways_bottom_up_x(n, x):
    nums = [1]
    if n == 0:
        return 1 
    for i in range(1, n+1):
        total = 0
        for j in x:
            if i - j >= 0:
                total += nums[i-j]
        nums.append(total)
    return nums[n]


print(num_ways_bottom_up_x(5, [1, 3, 5]))