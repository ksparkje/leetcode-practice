# 91. Decode Ways
# Medium
#
# 1293
#
# 1488
#
# Favorite
#
# Share
# A message containing letters from A-Z is being encoded to numbers using the
# following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given a non-empty string containing only digits, determine the total number of
# ways to decode it.
#
# Example 1:
#
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# Example 2:
#
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).


'''
if length == 1:
    try only from 1 to 9
else:
    try from 1 to 26

This won't work on cases like 000 or 101

'''
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0

        def dfs(idx):
            if idx == len_s:
                return 1
            if idx == len_s - 1:
                return 0 if s[idx] == '0' else 1
            if idx in visited:
                return visited[idx]

            ret = 0
            if s[idx] == '0':
                # sorta stupid...
                return ret
            elif '1' <= s[idx:idx+2] <= '26':
                ret += dfs(idx+1)
                ret += dfs(idx+2)
            else:
                ret += dfs(idx+1)

            visited[idx] = ret
            return ret

        len_s = len(s)
        visited = {}
        return dfs(0)


if __name__ == '__main__':
    s = Solution()

    print(s.numDecodings('226'))
    print(s.numDecodings('12'))
    print(s.numDecodings('000'))
    print(s.numDecodings('010'))
    print(s.numDecodings('101'))
    print(s.numDecodings('27'))















































