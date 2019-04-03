# 89. Gray Code
#
# The gray code is a binary numeral system where two successive values differ in only one bit.
#
# Given a non-negative integer n representing the total number of bits in the code,
# print the sequence of gray code. A gray code sequence must begin with 0.
#
# Example 1:
#
# Input: 2
# Output: [0,1,3,2]
# Explanation:
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
#
# For a given n, a gray code sequence may not be uniquely defined.
# For example, [0,2,3,1] is also a valid gray code sequence.
#
# 00 - 0
# 10 - 2
# 11 - 3
# 01 - 1

# Example 2:
#
# Input: 0
# Output: [0]
# Explanation: We define the gray code sequence to begin with 0.
#              A gray code sequence of n has size = 2n, which for n = 0 the size is 20 = 1.
#              Therefore, for n = 0 the gray code sequence is [0].


'''
Begin with simple case

0   0    00                            000
    1    01 ___________________        001
         11 From this mid point        011
         10 reverse the last digit     010 __________________________________________________
            and add one to the front   110 From the mid point, add 1 to the front to the reversed original
                                       111
                                       101
                                       100
'''

class Solution:
    def grayCode(self, n: int):
        so_far = [0]
        for idx in range(1, n+1):
            so_far += [1 << (idx-1) | item for item in reversed(so_far)]
        return so_far


