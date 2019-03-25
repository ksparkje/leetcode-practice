# 556. Next Greater Element III
# Medium
#
# 326
#
# 101
#
# Favorite
#
# Share
# Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.
#
# Example 1:
#
# Input: 12
# Output: 21
#
#
# Example 2:
#
# Input: 21
# Output: -1


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        given_number = list(str(n))

        idx = len(given_number) - 2

        while idx >= 0 and given_number[idx] >= given_number[idx+1]:
            idx -= 1

        if idx < 0:
            return -1

        swap_idx = len(given_number) - 1

        while swap_idx > idx and given_number[swap_idx] <= given_number[idx]:
            swap_idx -= 1

        given_number[idx], given_number[swap_idx] = given_number[swap_idx], given_number[idx]
        given_number[idx+1:] = given_number[idx+1:][::-1]
        given_number = int(''.join(given_number))

        return given_number if given_number != n and not given_number > (1 << 32) - 1 else -1



