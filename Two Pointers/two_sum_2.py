def two_sum(numbers, target):
    i = 0
    j = len(numbers) - 1
    while (i < j):
        if (numbers[i] + numbers[j] > target):
            j = j - 1
        elif (numbers[i] + numbers[j] < target):
            i = i + 1
        else:
            return [i+1,j+1]

print(two_sum([-1,0],-1)) 

