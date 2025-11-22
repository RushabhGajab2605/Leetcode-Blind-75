from collections import defaultdict

def maximumDistinctSubarraySum(nums,k):
    start = 0
    window_sum = 0
    max_sum = 0
    freq = defaultdict(int)

    for end in range (len(nums)):
        window_sum += nums[end]
        freq[nums[end]] += 1

        if (end - start + 1 == k): #Check that the window size is equal to k

            if (len(freq) == k): #Check for uniqueness of the elements in the window

                max_sum = max(max_sum,window_sum)

            freq[nums[start]] = freq[nums[start]] - 1
            if (freq[nums[start]] == 0):
                del freq[nums[start]]

            window_sum = window_sum - nums[start]
            start = start + 1

    return max_sum


print(maximumDistinctSubarraySum([1,5,4,2,9,9,9],3))