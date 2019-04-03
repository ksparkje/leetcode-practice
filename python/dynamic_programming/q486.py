# 486. Predict the Winner
# Medium
#
# Given an array of scores that are non-negative integers. Player 1 picks one of the numbers from
# either end of the array followed by the player 2 and then player 1 and so on. Each time a player
# picks a number, that number will not be available for the next player. This continues until all
# the scores have been chosen. The player with the maximum score wins.
#
# Given an array of scores, predict whether player 1 is the winner. You can assume each player plays
# to maximize his score.
#
# Example 1:
# Input: [1, 5, 2]
# Output: False
# Explanation: Initially, player 1 can choose between 1 and 2.
# If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5,
# then player 1 will be left with 1 (or 2).
# So, final score of player 1 is 1 + 2 = 3, and player 2 is 5.
# Hence, player 1 will never be the winner and you need to return False.
# Example 2:
# Input: [1, 5, 233, 7]
# Output: True
# Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7. No matter
# which number player 2 choose, player 1 can choose 233.
# Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.


# Its important to notice,
# that given A[i:j], function must return the possible score for the corresponding array.
# It should not care what the previous result is.
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        so_far = {}
        def compute_from_i_j(total_remaining, i, j):
            i_j = (i,j)
            if i_j in so_far:
                return so_far[i_j]
            if j - i == 0:
                so_far[i_j] = nums[i]
                return nums[i]

            remove_left_sum = total_remaining - compute_from_i_j(total_remaining - nums[i], i + 1, j)
            remove_right_sum = total_remaining - compute_from_i_j(total_remaining - nums[j], i, j - 1)

            max_sum = max(remove_left_sum, remove_right_sum)
            so_far[i_j] = max_sum
            return max_sum

        sum_nums = sum(nums)
        return compute_from_i_j(sum_nums, 0, len(nums) - 1) * 2 >= sum_nums




