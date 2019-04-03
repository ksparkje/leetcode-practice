# Reverse Integer
# Given 32 bit signed integer, reverse digits of an integer


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_neg = x < 0
        if is_neg:
            x = -x

        ret = 0
        while x:
            ret *= 10
            ret += x % 10
            x //= 10
        
        if ret > (1 << 32) - 1:
            return 0

        return -ret if is_neg else ret
            
            
        


