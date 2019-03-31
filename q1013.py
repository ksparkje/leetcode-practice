# 1013. Partition Array Into Three Parts With Equal Sum
# User Accepted: 2115
# User Tried: 2488
# Total Accepted: 2184
# Total Submissions: 4793
# Difficulty: Easy
# Given an array A of integers, return true if and only if we can partition the array into three
# non-empty parts with equal sums.
#
# Formally, we can partition the array if we can find indexes i+1 < j with (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])
#
#
#
# Example 1:
#
# Input: [0,2,1,-6,6,-7,9,1,2,0,1]
# Output: true
# Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

# Example 2:
#
# Input: [0,2,1,-6,6,7,9,-1,2,0,1]
# Output: false

# Example 3:
#
# Input: [3,3,6,5,-2,2,5,1,-9,4]
# Output: true
# Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4

'''
If I have the sum,
the target sum must be sum // 3. If divmod has remainder, return False

'''
from itertools import accumulate
from typing import List


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total = sum(A)

        quotient, remainder = divmod(total, 3)
        print(quotient)

        if remainder:
            return False

        acc = list(accumulate(A))
        acc_reversed = list(accumulate(A[::-1]))

        first_quot = acc.index(quotient) if quotient in acc else None
        reverse_quot = acc_reversed.index(quotient) if quotient in acc_reversed else None
        if reverse_quot is not None:
            reverse_quot = len(A) - reverse_quot - 1

        if first_quot is None:
            return False

        return first_quot < reverse_quot - 1


if __name__ == '__main__':
    input = [0,2,1,-6,6,7,9,-1,2,0,1]
    input = [3, 3, 6, 5, -2, 2, 5, 1, -9, 4]
    input = [0,2,1,-6,6,-7,9,1,2,0,1]
    s = Solution()

    print(s.canThreePartsEqualSum(input))























