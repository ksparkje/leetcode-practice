class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        :param nums:
        :return: length of the new nums
        '''

        '''
        gameplan: 
        Have two iterators from behind. Each time I see the same number, 
            move the front pointer until I see a new number. Swap that number
            with the back pointer. Move both pointer.
        Edge case: nums len <= 2
        '''

        if not nums:
            return 0

        cur_idx = 0

        for idx, item in enumerate(nums[1:], 1):
            if nums[cur_idx] != item:
                cur_idx += 1
                nums[cur_idx] = item
        return cur_idx + 1



