from collections import Counter

def isAnagram(s, t):
    freq_s = Counter(s)
    freq_t = Counter(t)
    if freq_s != freq_t:
        return False

    return True