# 188. Best Time to Buy and Sell Stock IV
# Hard
#
# 681
#
# 47
#
# Favorite
#
# Share
# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most k transactions.
#
# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
#
# Example 1:
#
# Input: [2,4,1], k = 2
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
# Example 2:
#
# Input: [3,2,6,5,0,3], k = 2
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
#              Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
from typing import List


'''
Nice intuitive solution
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/discuss/54172/Quick-n-easy-9-liner-in-Python-using-memo
'''
class Solution(object):
    def maxProfit(self, k, prices):
        def solve(prices, k, idx, memo={}):
            if idx <= 0 or not k:
                return 0
            if (k, idx) in memo:
                return memo[k, idx]
            no_sell = solve(prices, k, idx-1, memo)
            sell = 0
            for i in range(idx):
                sell = max(sell,
                           prices[idx] - prices[i] + solve(prices, k-1, i-1, memo)
                           )
            memo[k, idx] = max(sell, no_sell)
            return memo[k, idx]
        return solve(prices, k, len(prices) - 1)



