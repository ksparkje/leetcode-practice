# 322. Coin Change
# Medium
#
# You are given coins of different denominations and a total amount of money amount.
# Write a function to compute the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return -1.
#
# Example 1:
#
# Input: coins = [1, 2, 5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:
#
# Input: coins = [2], amount = 3
# Output: -1
# Note:
# You may assume that you have an infinite number of each kind of coin.
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        inf = float('inf')
        possible = [0] + [inf] * amount

        for amt in range(1, amount+1):
            possible[amt] = min(possible[amt - coin] + 1 if amt - coin >= 0 else inf
                                for coin in coins)

        return possible[amount] if possible[amount] != inf else -1

    def coinChangeNotSureWhy(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        visited = {}

        def dfs(remaining, num_coins, coin_idx):
            if remaining == 0:
                return num_coins
            if remaining < 0 or coin_idx == len(coins):
                return -1

            if remaining in visited:
                return visited[remaining]

            for idx, coin in enumerate(coins[coin_idx:], coin_idx):
                if remaining < coin:
                    return dfs(remaining, num_coins, idx+1)

                minimum_coin_from_here = dfs(remaining - coin, num_coins+1, idx)
                if minimum_coin_from_here != -1:
                    visited[remaining] = minimum_coin_from_here
                    return minimum_coin_from_here

            visited[remaining] = -1
            return -1

        return dfs(amount, 0, 0)


if __name__ == '__main__':
    s = Solution()
    print(s.coinChange([1,2,5], 11))





