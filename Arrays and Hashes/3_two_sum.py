def twoSum(nums, target):
    index_two_dictionary = {}

    for index,num in enumerate(nums):

        complement = target - num

        if (complement in index_two_dictionary):

            return [index_two_dictionary[complement],index]
        
        index_two_dictionary[num] = index

print(twoSum([2,7,11,15],9))
print(twoSum([3,2,4],6))
print(twoSum([3,3],6))