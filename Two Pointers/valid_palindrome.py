def isPalindrome(s):
    only_alpha = ""
    for chr in s:
        if chr.isalnum():
            only_alpha += chr.lower()
    
    i = 0
    j = len(only_alpha)-1
    if (only_alpha == " "):
        return True
    while (i < j):
        if (only_alpha[i] == only_alpha[j]):
            i += 1
            j -= 1
        else:
            return False

    return True

s = "0P"
print(isPalindrome(s))
