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


if __name__ == '__main__':
    s = Solution()
    print(s.num_with_one_repeated_digit(20))
    print(s.num_with_one_repeated_digit(100))
    print(s.num_with_one_repeated_digit(1000))

