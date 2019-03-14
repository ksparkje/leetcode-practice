# 46. Permutations
#
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]


class Solution:
    def permute(self, nums):
        def get_permute():
            if not nums:
                yield []
                return

            else:
                for idx, item in enumerate(nums):
                    for rest in self.permute(nums[:idx] + nums[idx+1:]):
                        yield [item] + rest

        return [item for item in get_permute()]


if __name__ == '__main__':
    s = Solution()
    print(s.permute([1,2,3,4,5]))
