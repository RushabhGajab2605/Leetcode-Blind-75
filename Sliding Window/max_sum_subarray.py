def maxSumSubarray(nums,k):
    start = 0
    window_sum = 0
    max_sum = 0

    for end in range (len(nums)):

        window_sum = window_sum + nums[end]

        if (end >= k - 1):

            max_sum = max(max_sum, window_sum)
            window_sum = window_sum - nums[start]
            start = start + 1

    return max_sum


print(maxSumSubarray([2, 1, 5, 1, 3, 2],3))
