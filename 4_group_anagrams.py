#My solution: Not efficient
# from collections import Counter, defaultdict

# def groupAnagrams(strs):
    # new_strs = []
    # for str in strs:
    #     new_strs.append(tuple(sorted(str)))

    # unique_anagrams = set(tuple(new_strs))

    # anagram_dict = {}

    # for str in strs:
    #     for un_an in unique_anagrams:
    #         if Counter(str) == Counter(un_an):
    #             if (un_an not in anagram_dict):
    #                 anagram_dict[un_an] = [str]
    #             else:
    #                 anagram_dict[un_an].append(str)

    # return(list(anagram_dict.values()))


# Solution using defaultdict:
# from collections import Counter, defaultdict

# def groupAnagrams(strs):

#     anagram_dict = defaultdict(list)

#     for word in strs:

#         key = tuple(sorted(word))
#         if key not in anagram_dict:
#             anagram_dict[key] = [word]
#         else:
#             anagram_dict[key].append(word)
    
#     return(list(anagram_dict.values()))

#Correctly using defaultdict
from collections import defaultdict
def groupAnagrams(strs):

    anagram_dict = defaultdict(list)

    for word in strs:
        key = tuple(sorted(word))
        anagram_dict[key].append(word)
        
    return(list(anagram_dict.values()))

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))




    









