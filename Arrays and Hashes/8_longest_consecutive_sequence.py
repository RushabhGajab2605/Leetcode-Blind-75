def longestConsecutive(nums):
    if (not nums):
        return 0
    
    unique_sorted = set(nums)
    unique_list = list(unique_sorted)
    unique_list.sort()
    curr = 1
    longest = 1
    for i in range(1,len(unique_list)):
        if unique_list[i] == unique_list[i-1] + 1 :
            curr += 1
        else:
            longest = max(curr, longest)
            curr = 1
            
    return max(longest,curr)

print(longestConsecutive([1,2,3,10,11,12]))
# print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
# print(longestConsecutive([1,0,1,2]))