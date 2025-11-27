def characterReplacement(s,k):
    start = 0
    n = len(s)
    char_frequency = {}
    longest = 0

    for end in range (n):
        if (s[end] not in char_frequency):
            char_frequency[s[end]] = 1
        else:
            char_frequency[s[end]] += 1
        
        while((((end - start) + 1) - max(char_frequency.values())) > k):
            char_frequency[s[start]] -= 1
            start += 1
            

        longest = max(longest, ((end - start) + 1))

    return longest

s = "AABABBA"
k = 1
print(characterReplacement(s,k))
