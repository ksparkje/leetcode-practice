# 201. Bitwise AND of Numbers Range
# Medium
#
# 373
#
# 51
#
# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the
# bitwise AND of all numbers in this range, inclusive.
#
# Example 1:
#
# Input: [5,7]
# Output: 4
# Example 2:
#
# Input: [0,1]
# Output: 0
'''
Suppose m = 4, n = 7
4    1 0 0
5    1 0 1
6    1 1 0
7    1 1 1

Push bit right until 4 == 7...
4    1 0 0  =>  1 0  => 1
5    1 0 1  =>  1 0  => 1
6    1 1 0  =>  1 1  => 1
7    1 1 1  =>  1 1  => 1

3    0 1 1
4    1 0 0
5    1 0 1
6    1 1 0
------------ => 0

'''
from functools import reduce


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == 0:
            return 0
        count = 0
        while m < n:
            m >>= 1
            n >>= 1
            count += 1
        return m << count

    def rangeBitwiseAndNaive(self, m: int, n: int) -> int:
        return reduce(lambda x, y: x & y, range(m, n+1))


if __name__ == '__main__':
    s = Solution()
    print(s.rangeBitwiseAndNaive(3, 10))
    print(s.rangeBitwiseAnd(3, 10))