def lengthOfLongestSubstring(str):
    left = 0
    longest = 0
    seen = set()
    n = len(str)

    for right in range (n):

        while (str[right] in seen):
            seen.remove(str[left])
            left = left + 1


        seen.add(str[right])
        longest = max(longest, right - left + 1)
        
    return longest


s = "pwwkew"
print(lengthOfLongestSubstring(s))