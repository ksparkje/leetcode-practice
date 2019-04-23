# 188. Best Time to Buy and Sell Stock IV
# Hard
#
# 681
#
# 47
#
# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most k transactions.
#
# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock
# before you buy again).
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
I can either choose to trade (sell) today, or not

Given ith in [0: today]:
    Try buying on ith day and selling it today
    This makes one trade, so compute the rest of the trades recursively
'''
class Solution2:
    def maxProfit(self, k, prices):

        def f(sell_date, num_trades):

            if sell_date <= 0 or num_trades == 0:
                return 0

            if (sell_date, num_trades) in visited:
                return visited[sell_date, num_trades]

            not_today = f(sell_date - 1, num_trades)
            today = 0

            for buy_date in range(sell_date):
                today = max(today,
                            prices[sell_date] - prices[buy_date] + f(buy_date - 1, num_trades - 1)
                            )

            visited[sell_date, num_trades] = max(today, not_today)

            return visited[sell_date, num_trades]

        visited = {}
        return f(len(prices)-1, k)

    def maxProfitSecondTry(self, k, prices):
        len_price = len(prices)

        if len_price < 2:
            return 0
        # k is big enougth to cover all ramps.
        if k >= len_price / 2:
            return sum(i - j
                       for i, j in zip(prices[1:], prices[:-1]) if i - j > 0)

        global_profit = [[0] * len_price for _ in range(k+1)]

        for num_trade in range(1, k+1):
            local_profit = [0] * len_price
            for today_idx, today_price in enumerate(prices[1:], 1):
                yesterday_price = prices[today_idx - 1]
                today_gain = today_price - yesterday_price
                # print(local_profit)
                # print(global_profit)
                local_profit[today_idx] = max(local_profit[today_idx - 1] + today_gain,
                                              global_profit[num_trade - 1][today_idx - 1],
                                              global_profit[num_trade - 1][today_idx - 1] + today_gain
                                              )
                global_profit[num_trade][today_idx] = max(local_profit[today_idx],
                                                          global_profit[num_trade][today_idx - 1])

        return global_profit[k][-1]


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


def maxProfit4(self, k, prices):
    n = len(prices)
    if n < 2:
        return 0
    # k is big enougth to cover all ramps.
    if k >= n / 2:
        return sum(i - j
                   for i, j in zip(prices[1:], prices[:-1]) if i - j > 0)
    globalMax = [[0] * n for _ in range(k + 1)]
    for i in range(1, k + 1):
        # The max profit with i transations and selling stock on day j.
        localMax = [0] * n
        for j in range(1, n):
            profit = prices[j] - prices[j - 1]
            localMax[j] = max(
                # We have made max profit with (i - 1) transations in
                # (j - 1) days.
                # For the last transation, we buy stock on day (j - 1)
                # and sell it on day j.
                globalMax[i - 1][j - 1] + profit,
                # We have made max profit with (i - 1) transations in
                # (j - 1) days.
                # For the last transation, we buy stock on day j and
                # sell it on the same day, so we have 0 profit, apparently
                # we do not have to add it.
                globalMax[i - 1][j - 1],  # + 0,
                # We have made profit in (j - 1) days.
                # We want to cancel the day (j - 1) sale and sell it on
                # day j.
                localMax[j - 1] + profit)
            globalMax[i][j] = max(globalMax[i][j - 1], localMax[j])
    return globalMax[k][-1]


if __name__ == '__main__':
    s = Solution2()
    print(s.maxProfitSecondTry(2, [2,3,4,0,8,7,6,10]))














