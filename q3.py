# 3. Longest Substring Without Repeating Characters

# Example 1:
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        starting_index, max_len = 0, 0
        so_far = {}
        for i, character in enumerate(s):
            if character in so_far and so_far[character] >= starting_index:
                starting_index = so_far[character] + 1
            so_far[character] = i
            max_len = max(max_len, i - starting_index + 1)

        return max_len


