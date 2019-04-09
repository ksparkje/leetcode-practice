# 90. Subsets II
#
# Given a collection of integers that might contain duplicates, nums, return
# all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
# Input: [1,2,2]
# Output:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]


'''
[1, 2, 2, 2]

[1]
[1, 2]
[1, 2, 2]
[1, 2, 2, 2]
[2]
[2, 2]
[2, 2, 2]

https://leetcode.com/problems/subsets-ii/discuss/229447/Python-backtracking-(general-approach)-beats-100
'''
class Solution:
    def subsetsWithDup(self, nums):
        def backtracking(start_idx, temp):
            so_far.append(temp)
            for idx, item in enumerate(nums[start_idx:], start_idx):
                if idx == start_idx or item != nums[idx-1]:
                    backtracking(idx + 1, temp + [item])

        nums.sort()
        so_far = []
        backtracking(0, [])
        return so_far


def backtrack(nums, res, temp, start):
    res.append(temp)
    for i in range(start, len(nums)):
        # Skip duplicate numbers
        if not (i > start and nums[i-1] == nums[i]):
            backtrack(nums, res, temp + [nums[i]], i+1)


class Solution2(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        backtrack(nums, res, [], 0)
        return res


class Solution3:
    def subsetsWithDup(self, nums):
        if not nums:
            return []
        nums.sort()
        res, cur = [[]], []
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                cur = [item + [num] for item in cur]
            else:
                cur = [item + [num] for item in res]
            res += cur
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.subsetsWithDup([1,2,2]))
