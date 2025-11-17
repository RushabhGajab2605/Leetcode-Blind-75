from collections import Counter
def topKFrequent(nums,k):
    ans = []
    nums_freq = Counter(nums)
    sorted_nums_freq = sorted(nums_freq.items(), key=lambda x: x[1])
    for i in range (k):
        ans.append(sorted_nums_freq.pop()[0])
    return ans

print(topKFrequent([1,1,1,2,2,3],2))
