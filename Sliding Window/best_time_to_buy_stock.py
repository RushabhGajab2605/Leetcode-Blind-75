# First Approach -- Wrong!
# def maxProfit(prices):

#     buy = 0
#     n = len(prices)
#     max_profit = 0
#     max_sell = 0

#     for sell in range (n):

#         if (prices[buy] > prices[sell]):
#             buy += 1

#         if (prices[sell] > prices[buy] and buy < sell):
#             max_sell = max(max_sell,prices[sell])

#     max_profit = max_sell - prices[buy]

#     if (max_profit > 0):
#         return max_profit
#     return 0


# Correct Approach
def maxProfit(prices):

    buy = 0
    n = len(prices)
    max_profit = 0
    
    for sell in range (n):

        if (prices[buy] > prices[sell]):
            buy = sell

        else:
            curr_profit = prices[sell] - prices[buy]
            max_profit = max(max_profit,curr_profit)

    return max_profit



prices = [7,6,4,3,1]
print(maxProfit(prices))