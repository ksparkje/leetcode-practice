# 334. Increasing Triplet Subsequence
# Medium
#
# Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.
#
# Formally the function should:
#
# Return true if there exists i, j, k
# such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
# Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.
#
# Example 1:
#
# Input: [1,2,3,4,5]
# Output: true
# Example 2:
#
# Input: [5,4,3,2,1]
# Output: false
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        first, second = None, None

        for item in nums:
            if first is None:
                first = item
            else:
                if item <= first:
                    first = item
                else:
                    if second is None or second >= item:
                        second = item
                    else:
                        return True

        return False

    def increasingTripletBetter(self, nums: List[int]) -> bool:

        first, second = float('inf'), float('inf')

        for item in nums:
            if item <= first:
                first = item
            elif item <= second:
                second = item
            else:
                return True

        return False


if __name__ == '__main__':
    s = Solution()
    print(s.increasingTriplet([1,2,3,4,5]))
    print(s.increasingTriplet([1,2,0,1]))
    print(s.increasingTriplet([1,0,1]))
    print(s.increasingTriplet([4,2,0,1]))
    print(s.increasingTriplet([3,2,0,1,2]))
    print(s.increasingTriplet([3,2,0,1,2]))
    print(s.increasingTriplet([1,0]))

