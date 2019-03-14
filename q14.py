# 14. Longest Common Prefix
# Easy
#
# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ''

        min_string = min(strs)
        max_string = max(strs)

        for idx, char in enumerate(min_string):
            if char != max_string[idx]:
                return min_string[:idx]

        return min_string


