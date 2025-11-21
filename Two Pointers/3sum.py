def threeSum(nums):
    res = []
    nums.sort()
    n = len(nums)

    for i in range (n):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        l = i + 1
        r = n - 1
        while (l < r):
            three_sum = nums[i] + nums[r] + nums[l]
            if (three_sum > 0):
                r = r - 1
            elif (three_sum < 0):
                l = l + 1
            else:
                res.append([nums[i],nums[l],nums[r]])
                while l < r and nums[l] == nums[l+1]:
                    l = l + 1
                while l < r and nums[r] == nums[r-1]:
                    r = r - 1

                l = l + 1
                r = r - 1
    
    return res

print(threeSum([-1,0,1,2,-1,-4]))