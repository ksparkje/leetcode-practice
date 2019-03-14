def argsort(seq):
    # http://stackoverflow.com/questions/3071415/efficient-method-to-calculate-the-rank-vector-of-a-list-in-python
    return sorted(range(len(seq)), key=seq.__getitem__)


class Solution(object):

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

        
        


