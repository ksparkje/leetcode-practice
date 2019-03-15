# 179. Largest Number
# Medium
#
# Given a list of non negative integers, arrange them such that they form the largest number.
#
# Example 1:
#
# Input: [10,2]
# Output: "210"

# Example 2:
#
# Input: [3,30,34,5,9]
# Output: "9534330"

from typing import List

class NewString:
    def __init__(self, s):
        self.s = s

    def __lt__(self, other):
        return self.s + other.s < other.s + self.s


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        all_nums_in_str = list(map(lambda x: NewString(str(x)), nums))
        return ''.join(map(lambda x: x.s, sorted(all_nums_in_str, reverse=True))).lstrip('0') or '0'


if __name__ == '__main__':
    s = Solution()
    print(s.largestNumber([10,2]))
    print(s.largestNumber([2,3,43, 44, 53, 93, 990, 972]))
    test_value = [41,23,87,55,50,53,18,9,39,63,35,33,54,25,
                  26,49,74,61,32,81,97,99,38,96,22,95,35,57,80,80] #,16,22,17,13,89,11,75,98,57,81,69,8,10,85,13,49,66,94,80,25,13,85,55,12,87,50,28,96,80,43,10,24,88,52,16,92,61,28,26,78,28,28,16,1,56,31,47,85,27,30,85,2,30,51,84,50,3,14,97,9,91,90,63,90,92,89,76,76,67,55]
    print(s.largestNumber(test_value))
