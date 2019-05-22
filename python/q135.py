# 135. Candy
# Hard

# There are N children standing in a line. Each child is assigned a rating value.

# You are giving candies to these children subjected to the following requirements:

# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?

# Example 1:

# Input: [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
# Example 2:

# Input: [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
#              The third child gets 1 candy because it satisfies the above two conditions.
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        left_to_right = []
        for idx, item in enumerate(ratings):
            if not idx or ratings[idx - 1] >= item:
                left_to_right += [1]
            else:
                left_to_right += [left_to_right[-1] + 1]

        right_to_left = []
        for idx, item in reversed(list(enumerate(ratings))):
            if idx == len(ratings) - 1 or ratings[idx + 1] >= item:
                right_to_left += [1]
            else:
                right_to_left += [right_to_left[-1] + 1]

        return sum([max(left, right)
                    for left, right in zip(left_to_right, reversed(right_to_left))])