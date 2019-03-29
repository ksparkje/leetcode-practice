# 161. One Edit Distance
# Medium
#
# Given two strings s and t, determine if they are both one edit distance apart.
#
# Note:
#
# There are 3 possiblities to satisify one edit distance apart:
#
# Insert a character into s to get t
# Delete a character from s to get t
# Replace a character of s to get t
# Example 1:
#
# Input: s = "ab", t = "acb"
# Output: true
# Explanation: We can insert 'c' into s to get t.
# Example 2:
#
# Input: s = "cab", t = "ad"
# Output: false
# Explanation: We cannot get t from s by only one step.
# Example 3:
#
# Input: s = "1203", t = "1213"
# Output: true
# Explanation: We can replace '0' with '1' to get t.


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # if s is none or t is none...
        if s == t:
            return False

        if len(s) < len(t):
            s, t = t, s

        if not t:
            return len(s) == 1

        if len(s) == len(t):
            count = 0
            for a, b in zip(s, t):
                if a != b:
                    count += 1
                if count > 1:
                    return False
            return True
        else:
            if len(s) - 1 != len(t):
                return False

            for idx, (a, b) in enumerate(zip(s,t)):
                # CORNER CASE, WHEN THE LAST CHARACTER FOR BOTH ARE THE SAME
                if idx == len(t)-1 and a == b:
                    return True
                if a != b:
                    break

            return s[idx+1:] == t[idx+1:] or s[idx+1:] == t[idx:]


class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t: return False
        i = 0
        while i < min(len(s),len(t)):
            if s[i] == t[i]:
                i += 1
            else:
                break
        return s[i+1:] == t[i+1:] or s[i:] == t[i+1:] or s[i+1:]==t[i:]


if __name__ == '__main__':
    s = Solution()
    print(s.isOneEditDistance('a', 'ac'))
    print(s.isOneEditDistance('acbd', 'acbda'))



