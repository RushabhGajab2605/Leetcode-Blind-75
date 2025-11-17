# --- Using Counter class ---

from collections import Counter

def containsDuplicate(nums):

    nums_frequency = Counter(nums)
    for nums in nums_frequency:
        if nums > 1:
            return False
    
    return True

# --- Using sets ---

# def containsDuplicate(nums):
#     if (len(nums) != len(set(nums))):
#         return True
#     return False

# --- Using sorting for efficient solution ---

# def containsDuplicate(nums):
#     nums.sort()
#     for i in range (1, len(nums)):
#         if (nums[i] == nums[i-1]):
#             return True
#     return False

# print(containsDuplicate([1,2,3,1]))



