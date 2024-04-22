# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Brute Force Solution:
def maxProfit1(price):
    max_profit = 0
    n = len(price)

    for i in range(n):
        for j in range(i+1, n):
            profit = price[j] - price[i]
            if profit > max_profit:
                max_profit = profit
                                                                        # Time Complexity: O(n^2)
    return max_profit                                                   # Space Complexity: O(1)

prices1 = [7,1,5,3,6,4]
print(maxProfit1(prices1))


# Better Solution:

def maxProfit2(price):
    min_price, max_profit = float('inf'), 0                             # float('inf') is a Python expression that represents positive infinity.
                                                                        
    for i in price:
        min_price = min(min_price, i)                                   
        max_profit = max(max_profit, i - min_price)                     # Time Complexity: O(n)
                                                                        # Space Complexity: O(1)
    return max_profit

prices2 = [7,1,5,3,6,4]
print(maxProfit2(prices2))
'''min_price is initialized to positive infinity (float('inf')) to ensure that
any price encountered in the prices array will be smaller than min_price.
During the iteration through the prices array, min(min_price, price) ensures that
min_price is updated to the minimum price encountered so far.'''