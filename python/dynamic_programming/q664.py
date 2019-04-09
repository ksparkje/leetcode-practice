# 664. Strange Printer
# Hard
#
# There is a strange printer with the following two special requirements:
#
# The printer can only print a sequence of the same character each time.
# At each turn, the printer can print new characters starting from and ending at any places, and will cover the original existing characters.
# Given a string consists of lower English letters only, your job is to count the minimum number of turns the printer needed in order to print it.
#
# Example 1:
# Input: "aaabbb"
# Output: 2
# Explanation: Print "aaa" first and then print "bbb".
# Example 2:
# Input: "aba"
# Output: 2
# Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.


'''
https://leetcode.com/problems/strange-printer/discuss/233067/Python.-Recursive-approach-with-memorization

The idea is, suppose I know the answer to [0:k-1] where k is the length of s.
Then, the current cost is + 1 previous, or use the same character's cost in the previous
index, call it j, + cost of [j+1 : k-1]
'''
class Solution:
    def strangePrinter(self, s: str) -> int:
        visited = {}

        def dfs(remaining_str):
            if not remaining_str:
                return 0

            if remaining_str in visited:
                return visited[remaining_str]

            cost_until_last = dfs(remaining_str[:-1]) + 1
            last_char = remaining_str[-1]
            for idx, char in enumerate(remaining_str[:-1]):
                if char == last_char:
                    cost_until_last = min(dfs(remaining_str[:idx+1]) +
                                          dfs(remaining_str[idx+1:-1]),
                                          cost_until_last)

            visited[remaining_str] = cost_until_last
            return cost_until_last

        return dfs(s)


if __name__ == '__main__':
    s = Solution()
    print(s.strangePrinter('aaabcdffa'))




















