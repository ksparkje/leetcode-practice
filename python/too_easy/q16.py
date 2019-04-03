# 3Sum Closest
# Given array of nums, and a target, find three integers in nums
#     such that the sum is cloeset to target

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        len_nums = len(nums)
        if len_nums == 0:
            return target
        elif len_nums == 1:
            return nums[0]
        elif len_nums == 2:
            return len_nums
            
            
            
        sorted_nums = sorted(nums)
        
    

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return target == 0

        nums_sorted = sort(nums)
        original_idx = argsort(nums)
        left, right = 0, len(nums)-1
    
        while left < right:
            cur_val = nums_sorted[left] + nums_sorted[right]
            if target < cur_val:
                right -= 1
            elif target == cur_val:
                return [original_idx[left], original_idx[right]]
            else:
                left += 1

        return False

        
