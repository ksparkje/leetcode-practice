# 937. Reorder Log Files

# You have an array of logs.  Each log is a space delimited string of words.
#
# For each log, the first word in each log is an alphanumeric identifier.  Then, either:
#
# Each word after the identifier will consist only of lowercase letters, or;
# Each word after the identifier will consist only of digits.
# We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed
# that each log has at least one word after its identifier.
#
# Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs
# are ordered lexicographically ignoring identifier, with the identifier used in case of ties.
# The digit-logs should be put in their original order.
#
# Return the final order of the logs.
#
#
#
# Example 1:
#
# Input: ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
# Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
#
#
# Note:
#
# 0 <= logs.length <= 100
# 3 <= logs[i].length <= 100
# logs[i] is guaranteed to have an identifier, and a word after the identifier.
from typing import List


class Value:
    def __init__(self, key, given_str: List[str], idx: int):
        self.key = key
        self.value = given_str
        self.idx = idx
        self.isalpha = given_str[0].isalpha()

    def __lt__(self, other) -> bool:

        if self.isalpha and other.isalpha:

            for v1, v2 in zip(self.value, other.value):
                if v1 == v2:
                    continue
                return v1 < v2

            # in case like [abc a] vs [abc a a]
            if len(self.value) != len(other.value):
                return len(self.value) < len(other.value)

            return self.key < other.key

        elif (not self.isalpha) and (not other.isalpha):
            return self.idx < other.idx

        return self.isalpha


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        if not logs:
            return []

        value_objects = []
        for idx, log in enumerate(logs):
            splitted = log.split(' ')
            key, value = splitted[0], splitted[1:]
            value_objects += [Value(key, value, idx)]

        value_objects.sort()

        return [item.key + ' ' + ' '.join(item.value) for item in value_objects]


if __name__ == '__main__':
    inputs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]

    s = Solution()
    print(s.reorderLogFiles(inputs))

























