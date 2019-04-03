# 22. Generate Parentheses
# Medium
#
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def f(open, close, so_far):
            if not close:
                yield so_far
                return

            if open:
                yield from f(open-1, close, so_far + '(')

            if open < close:
                yield from f(open, close-1, so_far + ')')

        result = [item for item in f(n, n, '')]
        return result


'''
'' -> (   -> ((     ->   (((      -> ((((
                    ->   (()      -> (()(
          -> ()     ->   ()(      -> ()((
                                  -> ()()
'''
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def f(open, close, temp, so_far):
            if not close:
                so_far += [temp]
                return
            if open:
                f(open-1, close, temp+'(', so_far)
            if close > open:
                f(open, close-1, temp+')', so_far)

        so_far = []
        f(n, n, '', so_far)

        return so_far

class SolutionDP:
    def generateParenthesis(self, n):
        parenthesis_by_row = [[] for _ in range(n+1)]
        parenthesis_by_row[0] = ['']
        for i in range(1, n+1):
            for j in range(i):
                parenthesis_by_row[i] += parenthesis_by_row[j] + parenthesis_by_row[i-j-1]




'''
USE Dynamic Programming!

Think of x axis as the number of pairs to go into a new parenthesis pair.
  j                    0                                       1                                   2                               3
  i                  
0 pair      None
1 pair      (all of 0 pair)
2 pair      (all of 0 pair) + all of 1 pair     (all of 1 pair) + all of 0 pair
3 pair      (all of 0 pair) + all of 2 pair     (all of 1 pair) + all of 1 pair    (all of 2 pair) + all of 0 pair
4 pair      (all of 0 pair) + all of 3 pair     (all of 1 pair) + all of 2 pair    (all of 2 pair) + all of 1 pair      (all of 3 pair) + all of 0 pair
'''
class SolutionDP:
    def generateParenthesis(self, n):
        so_far = [[] for _ in range(n+1)]
        so_far[0] = ['']
        for i in range(1, n+1):
            for j in range(0, i):
                # so_far[i] += ['(' + j_pair + ')' + rest for j_pair in so_far[j]
                #                                         for rest in so_far[i-j-1]]
                so_far[i] += ['(' + j_pair + ')' + rest for rest in so_far[i-j-1] for j_pair in so_far[j]]

        return so_far[n]


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))

    s = SolutionDP()
    print(s.generateParenthesis(3))
