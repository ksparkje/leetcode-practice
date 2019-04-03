# 1015. Smallest Integer Divisible by K
# User Accepted: 677
# User Tried: 1745
# Total Accepted: 710
# Total Submissions: 6398
# Difficulty: Medium
# Given a positive integer K, you need find the smallest positive integer N such that N is divisible by K,
# and N only contains the digit 1.
#
# Return the length of N.  If there is no such N, return -1.
#
#
#
# Example 1:
#
# Input: 1
# Output: 1
# Explanation: The smallest answer is N = 1, which has length 1.
# Example 2:
#
# Input: 2
# Output: -1
# Explanation: There is no such positive integer N divisible by 2.
# Example 3:
#
# Input: 3
# Output: 3
# Explanation: The smallest answer is N = 111, which has length 3.


'''
Interesting problem

Suppose K = 6
                                                diff
1           % 6 =               1 % 6 = 1
11          % 6 =               5 % 6 = 5         4
(100 + 11)  % 6 = (4 + 5) % 6 = 9 % 6 = 3         4 (from 5 to 9, before mod 6)
111         % 6 = above               = 3
1111        % 6 = (1000 + 111) % 6    = 1         4 (from 3 to 7, before mod 6)
'''
class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:

        # Don't do this... re-write please

        def is_one_only(val):
            if val == 0:
                return False

            while val:
                val, rem = divmod(val, 10)
                if rem != 1:
                    return False

            return True

        if K % 2 == 0:
            return -1

        guess = 1

        while guess < (1 << 64):
            quot, rem = divmod(guess, K)
            if rem == 0:
                if is_one_only(guess):
                    return len(str(guess))
            guess = guess * 10 + 1

        return -1




if __name__ == '__main__':
    s = Solution()
    print(s.smallestRepunitDivByK(17))











