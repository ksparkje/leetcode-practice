# 910. Smallest Range II
# Given an array A of integers, for each integer A[i] we need to choose either x = -K or x = K, and add x to A[i] (only once).
# After this process, we have some array B.
# Return the smallest possible difference between the maximum value of B and the minimum value of B.


class Solution:
    def smallestRangeII(self, A, K) -> int:
        A.sort()
        if len(A) <= 2:
            return 0 if max(A) - min(A) <= K else max(A) - min(A) - K

        low_diff = abs(A[1] - A[0])
        high_diff = abs(A[-1] - A[-2])

        if low_diff > high_diff:
            # better to move the min by K
            if low_diff > K:
                return A[-1] - (A[0] + K)
            else:
                return A[-1] - A[1]
        else:
            if high_diff > K:
                return A[-1] - K - A[0]
            else:
                return A[-2] - A[0]


if __name__ == '__main__':
    s = Solution()
    print(s.smallestRangeII([0], 2))
    print(s.smallestRangeII([0, 2], 2))
    print(s.smallestRangeII([0, 2, 8], 2))
    print(s.smallestRangeII([0, 2, 4, 8], 2))
    print(s.smallestRangeII([1, 3, 5, 10], 4))

