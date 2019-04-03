# 464. Can I Win
# Medium
#
# In the "100 game," two players take turns adding, to a running total, any integer from 1..10.
# The player who first causes the running total to reach or exceed 100 wins.
#
# What if we change the game so that players cannot re-use integers?
#
# For example, two players might take turns drawing from a common pool of numbers of 1..15 without
# replacement until they reach a total >= 100.
#
# Given an integer maxChoosableInteger and another integer desiredTotal, determine if the first player
# to move can force a win, assuming both players play optimally.
#
# You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will
# not be larger than 300.


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        so_far = {}
        choosable_integers = [i for i in range(1, maxChoosableInteger+1)]

        def can_win(choosable, remaining):
            # return True if winnable
            key = tuple(choosable)

            if key in so_far:
                return so_far[key]

            if max(choosable) >= remaining:
                return True

            if all(can_win(choosable[:i] + choosable[i+1:], remaining - item)
                   for i, item in enumerate(choosable)):
                so_far[key] = False
                return False

            else:
                so_far[key] = True
                return True

        return can_win(choosable_integers, desiredTotal)



class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        '''
        Define a hash such that it returns True if win-able from that point else False
        '''
        so_far = {}
        def helper(to_choose_from, remaining_total):
            hash_key = tuple(to_choose_from)
            if hash_key in so_far:
                return so_far[hash_key]
            if max(to_choose_from) >= remaining_total:
                so_far[hash_key] = True
                return True
            if all(helper(to_choose_from[:i] + to_choose_from[i+1:],
                          remaining_total - to_choose_from[i])
                   for i in range(len(to_choose_from))):
                so_far[hash_key] = False
                return False
            so_far[hash_key] = True
            return True

        to_choose_from = list(range(1, maxChoosableInteger+1))
        if sum(to_choose_from) < desiredTotal:
            return False
        return helper(to_choose_from, desiredTotal)


if __name__ == '__main__':
    s = Solution()
    print(s.canIWin(4, 10))
