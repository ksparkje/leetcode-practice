# 137. Single Number II
# Medium
#
# Given a non-empty array of integers, every element appears three times
# except for one, which appears exactly once. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
#
# Example 1:
#
# Input: [2,2,3,2]
# Output: 3
# Example 2:
#
# Input: [0,1,0,1,0,1,99]
# Output: 99


'''
Think outside the box!

Usual XOR doesn't work obviously, but if we can count % 3, for each bit, then
maybe it's possible?

2, 2, 3, 2 =>
              1 0
              1 0
              1 1
              1 0
------------------
              4 1 % 3
------------------
              1 1


0, 1, 0, 1, 0, 1, 3 =>
                            0
                            1
                            0
                            1
                            0
                            1
                        1   1
                        -----
                        1   4 % 3
                        -----
                        1   1
'''
from typing import List

'''
SMARTEST BITWISE IDEA EVER!!! 
'''
class Solution:
    def singleNumber(self, nums):
        one, two = 0, 0
        for x in nums:
            ''' one turns on/off, 
                two turns on if we have seen it before; one will have x
                three turns on if x was seen in two previously
            '''
            one, two, three = one ^ x, two | (one & x), two & x
            # print(one, two, three)
            one, two = one & ~three, two & ~three
            # print(one, two)
        return one


class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        for idx in range(32):
            count = 0
            for item in nums:
                if (item >> idx) & 1:
                    count += 1
            answer |= (count % 3) << idx

        return answer if answer < (1 << 31) else answer - (1 << 32)


if __name__ == '__main__':
    s = Solution()
    # print(s.singleNumber([0,1,0,1,0,1,99]))
    print(s.singleNumber([2,2,2,3,1,1,1]))























