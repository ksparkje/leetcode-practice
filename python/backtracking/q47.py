# 47. Permutations II
#
# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
#
# Example:
#
# Input: [1,1,2]
# Output:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]

'''
[1, 1, 2] =>
    [1, 1, 2]
    [1, 2, 1]
    [2, 1, 1]
'''
class Solution:
    def permuteUnique(self, nums):
        def helper(remaining):
            if not remaining:
                yield []
                return
            visited = set()
            for idx, item in enumerate(remaining):
                if item not in visited:
                    visited.add(item)
                    for rest in helper(remaining[:idx] + remaining[idx+1:]):
                        yield [item] + rest

        return [item for item in helper(nums)]


if __name__ == '__main__':
    s = Solution()
    print(s.permuteUnique([1, 1, 2, 3]))

