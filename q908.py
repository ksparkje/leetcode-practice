# 908. Smallest Range I
# Difficulty: Easy
# Given an array A of integers, for each integer A[i] we may choose any x with -K <= x <= K, and add x to A[i].
#
# After this process, we have some array B.
#
# Return the smallest possible difference between the maximum value of B and the minimum value of B.
#
#
# Example 1:
#
# Input: A = [1], K = 0
# Output: 0
# Explanation: B = [1]

# Example 2:
#
# Input: A = [0,10], K = 2
# Output: 6
# Explanation: B = [2,8]
# Example 3:
#
# Input: A = [1,3,6], K = 3
# Output: 0
# Explanation: B = [3,3,3] or B = [4,4,4]

class Solution:
    def smallestRangeI(self, A, K) -> int:
        min_a = min(A)
        max_a = max(A)

        if min_a + K >= max_a - K:
            return 0
        else:
            return max_a - K - (min_a + K)

if __name__ == '__main__':
    s = Solution()
    inputs = [([1], 0),
              ([0,10], 2),
              ([1,3,6], 3),
              ([2,3,10], 3),
              ([3,1,10], 4)]
    for A, K in inputs:
        print(s.smallestRangeI(A, K))