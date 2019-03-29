# 698. Partition to K Equal Sum Subsets
# Medium
#
# Given an array of integers nums and a positive integer k, find whether
# it's possible to divide this array into k non-empty subsets whose sums are all equal.
#
# Example 1:
#
# Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# Output: True
# Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

'''
Although may appear complex, it's actually quite simple.

Think of `k` as k buckets.
The idea is, try placing all the values in the `nums` to each of the bucket,
where buckets are sum of elements.


'''
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target, remainder = divmod(sum(nums), k)
        if remainder:
            return False

        nums.sort(reverse=True)

        # Keeping track of k buckets, so to speak
        buckets_sum_so_far = [0] * k

        def dfs(starting_index):
            if starting_index == len(nums):
                return True

            for idx, bucket in enumerate(buckets_sum_so_far):
                cur_elem = nums[starting_index]
                if bucket + cur_elem <= target:
                    buckets_sum_so_far[idx] += cur_elem
                    if dfs(starting_index+1):
                        return True
                    buckets_sum_so_far[idx] -= cur_elem
                    # If current bucket was 0, buckets to the right
                    # of myself would be all 0 as well...
                    if buckets_sum_so_far[idx] == 0:
                        break
            return False

        return dfs(0)

