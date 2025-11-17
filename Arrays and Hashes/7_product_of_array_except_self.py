
def productExceptSelf(nums):

    ans = []
    n = len(nums)
    left_prod = 1
    right_prod = 1
    left_prod_arr = [1]*n
    right_prod_arr = [1]*n

    for i in range (n):
        left_prod_arr[i] = left_prod # We will have to do this because doing this makes sure that when we reach the left extreme we will only consider product of right as the extreme will not have anything on its left
        left_prod = left_prod * nums[i]

    for i in range (n-1,-1,-1):
        right_prod_arr[i] = right_prod # We will have to do this because doing this makes sure that when we reach the right extreme we will only consider product of left as the extreme will not have anything on its right
        right_prod = right_prod * nums[i]

    for i in range (n):
        ans.append(left_prod_arr[i]*right_prod_arr[i])

    print(left_prod_arr)
    print(right_prod_arr)
    print(ans)

    return ans

productExceptSelf([1,2,3,4])




