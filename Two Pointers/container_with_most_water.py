def maxArea(height):
    i = 0
    j = len(height) - 1
    curr_area = 0
    max_area = 0
    while (i <= j):
        curr_area = min(height[i],height[j]) * (j-i)
        max_area = max(max_area,curr_area)
        i = i + 1
        j = j - 1

    return max_area

print(maxArea([1,8,6,2,5,4,8,3,7]))




