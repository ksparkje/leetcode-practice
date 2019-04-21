# 713. Subarray Product Less Than K

# Your are given an array of positive integers nums.
#
# Count and print the number of (contiguous) subarrays where the product
# of all the elements in the subarray is less than k.
#
# Example 1:
# Input: nums = [10, 5, 2, 6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
#   [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
# Note:
#
# 0 < nums.length <= 50000.
# 0 < nums[i] < 1000.
# 0 <= k < 10^6.
from typing import List


'''
Nice solution given by @awice https://leetcode.com/articles/subarray-product-less-than-k/

Intuition

For each right, call opt(right) the smallest left so that the product of the subarray 
nums[left] * nums[left + 1] * ... * nums[right] is less than k. opt is a monotone increasing 
function, so we can use a sliding window.

Algorithm

Our loop invariant is that left is the smallest value so that the product in the window 
prod = nums[left] * nums[left + 1] * ... * nums[right] is less than k.

For every right, we update left and prod to maintain this invariant. Then, the number of 
intervals with subarray product less than k and with right-most coordinate right, 
is right - left + 1 (Note: it's product less than). We'll count all of these for each 
value of right.

'''


'''
k: 9
A:     2   3   4   2   8    7
prod:  2   6   24
                4  8   64
                        8  56
                            7  

total number of subarray = 8?
[2], [3], [2,3], [4], [2], [4,2], [8], [7]
'''
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            # product less than k
            return 0

        prod_so_far = 1
        left_idx = count = 0
        for right_idx, item in enumerate(nums):
            prod_so_far *= item

            # prod must be strictly less
            while prod_so_far >= k:
                prod_so_far /= nums[left_idx]
                left_idx += 1

            count += right_idx - left_idx + 1

        return count


if __name__ == '__main__':

    s = Solution()
    print(s.numSubarrayProductLessThanK([2,3,4,2,8,7], 9))











