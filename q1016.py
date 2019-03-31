# Numbers with 1 repeat digit
#
# Given a positive integer N, return the number of positive integers less than
# or equal to N that have at least 1 repeated digit

# Example 1
# Input: 20
# Output: 1
# The only positive number <= 20 with at least 1 repated digit is 11

# Example 2
# Input: 100
# Output: 10
# The positive number <= 100 :=> 11, 22, 33 ... 99 100


'''
Lets try it like a graph problem.

With a given digit, say 1, build a possible node, such as 11, and check if it's possible.
Once created, put it in a visited, to not get confused later.
...


This seems stupid. Maybe a better way is to check if it has a repeated digit.
'''
from collections import Counter

class Solution:
    def num_with_one_repeated_digit(self, n):
        '''
        :param n:
        :return:
        '''

        def check_repeated_digit(x):
            counts = Counter(str(x))
            return max(counts.values()) >= 2

        return sum(check_repeated_digit(i) for i in range(1, n+1))


class SolutionFeng(object):
    def numDupDigitsAtMostN(self, N):
        """
        :type N: int
        :rtype: int
        """
        def helper(n,used):
            if not used:
                if n == 0:
                    return 0
                if n == 1:
                    return 9
                res = 9
                tmp = 9
                while n > 1:
                    res *= tmp
                    n -= 1
                    tmp -= 1
                return res
            else:
                N = 10-used
                res = 1
                for _ in range(n):
                    res *= N
                    N -= 1
                return res
        if N < 11:
            return 0
        res = 0
        l = len(str(N))-1
        while l:
            res += helper(l,0)
            l -= 1
        # print(res)
        lenN = len(str(N))
        l = lenN-1
        used = set()
        total = N
        flag = False
        while l:
            digit = N/(10**(l))
            if digit in used:
                flag = True
            used.add(digit)
            # print(digit,l,used,res)
            if l == lenN-1:
                res += (digit-1)*helper(l,lenN-l)
            else:
                for i in range(digit):
                    if i not in used:
                        res += helper(l,lenN-l)
            if flag:
                break
            l -= 1
            N %= (10**(l+1))
        # print(res)
        used = set(str(total)[:-1])
        if len(used) != len(str(total))-1:
            return total-res
        N = total/10*10
        while N <= total:
            if str(N%10) not in used:
                res += 1
            N += 1
        return total-res



if __name__ == '__main__':
    s = Solution()
    print(s.num_with_one_repeated_digit(20))
    print(s.num_with_one_repeated_digit(100))
    print(s.num_with_one_repeated_digit(1000))

