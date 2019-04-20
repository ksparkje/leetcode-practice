# 338. Counting Bits

# Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num
# calculate the number of 1's in their binary representation and return them as an array.
#
# Example 1:
#
# Input: 2
# Output: [0,1,1]
# Example 2:
#
# Input: 5
# Output: [0,1,1,2,1,2]
# Follow up:
#
# It is very easy to come up with a solution with run time O(n*sizeof(integer)).
# But can you do it in linear time O(n) /possibly in a single pass?
# Space complexity should be O(n).
# Can you do it like a boss? Do it without using any builtin function like __builtin_popcount
# in c++ or in any other language.
from typing import List


'''
0    1    2    3    4    5    6    7
0    1    10   11   100  101  110  111

8    9    10   11   12   13   14   15
1000 1001 1010 1011 1100 1101 1110 1111
'''
class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return []

        cur_array = [0, 1]
        i = 0

        while (1 << i) <= num:
            cur_array += [item + 1 for item in cur_array]
            i += 1

        return cur_array[:num+1]


if __name__ == '__main__':

    s = Solution()
    print(s.countBits(1))
    print(s.countBits(4))
    print(s.countBits(7))
    print(s.countBits(8))
    print(s.countBits(15))
    print(s.countBits(16))


