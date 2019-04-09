# 32. Longest Valid Parentheses
# Hard

# Given a string containing just the characters '(' and ')', find
# the length of the longest valid (well-formed) parentheses substring.
#
# Example 1:
#
# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
# Example 2:
#
# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"


'''
It's important to remember: stack needs to be kept non-empty
'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0

        longest_so_far = 0
        stack = [0]

        for idx, item in enumerate(s):
            if item == '(':
                # appending 2 doesn't work!
                stack.append(0)
            else:
                if len(stack) > 1:
                    this_height = stack.pop() + 2
                    stack[-1] += this_height
                    longest_so_far = max(stack[-1], longest_so_far)
                else:
                    stack = [0]

        return longest_so_far


if __name__ == '__main__':
    input = "()())"
    s = Solution()
    print(s.longestValidParentheses(input))





