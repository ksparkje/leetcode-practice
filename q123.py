# 123. Best Time to Buy and Sell Stock III
# Hard
#
# 932
#
# 53
#
# Favorite
#
# Share
# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most two transactions.
#
# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
#
# Example 1:
#
# Input: [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
#              Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
# Example 2:
#
# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
#              Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
#              engaging multiple transactions at the same time. You must sell before buying again.
# Example 3:
#
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
from typing import List


# EPI Q 5.7
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = [0] * len(prices)
        min_so_far = prices[0]
        for idx, p in enumerate(prices[1:], 1):
            min_so_far = min(min_so_far, p)
            max_profit[idx] = max(p - min_so_far, max_profit[idx-1])

        max_so_far = prices[-1]
        for idx, p in reversed(list(enumerate(prices[2:], 2))):
            max_so_far = max(max_so_far, p)
            max_profit[idx] = max(max_so_far - p + max_profit[idx-1], max_profit[idx])

        return max(max_profit)


if __name__ == '__main__':
    s = Solution()
    input = [3, 2, 6, 5, 0, 3]
    print(s.maxProfit(input))

