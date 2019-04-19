# 930. Binary Subarrays With Sum
# Medium
#
# 193
#
# 11
#
# In an array A of 0s and 1s, how many non-empty subarrays have sum S?
#
#
# Example 1:
#
# Input: A = [1,0,1,0,1], S = 2
# Output: 4
# Explanation:
# The 4 subarrays are bolded below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
#
#
# Note:
#
# A.length <= 30000
# 0 <= S <= A.length
# A[i] is either 0 or 1.
from typing import List
from collections import Counter


class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        counter = Counter({0:1})
        sum_so_far = 0
        count = 0

        for item in A:
            sum_so_far += item
            count += counter[sum_so_far - S]
            counter[sum_so_far] += 1

        return count


if __name__ == '__main__':
    s = Solution()
    print(s.numSubarraysWithSum(A=[1,0,1,0,1], S=2))



































