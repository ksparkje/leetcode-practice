# 907. Sum of Subarray Minimums
# Medium
#
# Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.
#
# Since the answer may be large, return the answer modulo 10^9 + 7.

# Example 1:
#
# Input: [3,1,2,4]
# Output: 17
# Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.


'''
중요: 질문의 요점은 최저점임...
다시말해, 인덱스 i-k에서 부터 i+j까지, 나의 엘리멘트가 저점 인가를 파악하는것이 요지...
그렇다면, 왼쪽에서부터 어디까지 나보다 큰지(-k) 알고, 오른쪽으로 어디까지 나보다 큰지(j) 알면, 나 본 지점의
총 길이는, k * j 이다...
이 질문에 답은 Keep a stack that has non-decreasing elements, such that if
this stack is empty, it implies that my current elem is the smallest of all elem seen so far,
so keep -1 as its index. Else, the elem left of myself is the first elem smaller than me.
When we pop off an elem from the stack, we keep track of that elem's right side.
The elem about to pushed in, when popping off, is the first elem that's smaller than me on the
right side. So, I can keep track of my right side distance that way!

e.g [3, 1, 2, 4]
----------------------
i = 0, [3]
----------------------
Now we come to see `1`.
3 is smaller than 1, pop the `3`.
3 was relevant from i = -1 to i = 0 => left_side = [-1:0], right_side = [0:0]
i = 1, [1]
---------------------------------------------------
i = 2, [1, 2]
i = 3, [1, 2, 4]
---------------------------------------------------
i = 4, Now time to count
For elem 1, it was relevant from left side of [-1:1] and right side [1:4]
Therefore, the count for elem 1 is (2 * 3)
For elem 2, it was relevant from left side of [1:2] and right side [2:4]
Therefore, the count for elem 2 is (1 * 2)
For elem 4, it was relevant from left side of [2:3] and right side [3:4]
Therefore, the count for elem 4 is (1 * 1)

So the answer would be 3 + 4 + 2*2 + 1*(2 * 3) = 17

When we actually do this, we tend to push the index of elem, instead of elem itself

Nice explanation
https://leetcode.com/problems/sum-of-subarray-minimums/discuss/178876/stack-solution-with-very-detailed-explanation-step-by-step

Possibly better
https://leetcode.com/problems/sum-of-subarray-minimums/discuss/170750/C++JavaPython-Stack-Solution
'''


'''
Gameplan:
Keep a non-decreasing stack
As soon as I hit a lower number than what is the most right in the stack,
pop the left ones while it's lower and record
'''
class Solution:
    '''
    Super nice solution
    [1, 2, 3, 4, 5]

    (*) left
    [1, 1, 1, 1, 1]

    (**) right
    Notice it's the inverse. Keep a non-decreasing stack from the reverse side.
    [5, 4, 3, 2, 1]
    '''
    def DiscussionSumSubarrayMins(self, A):
        n, mod = len(A), 10**9 + 7
        left, right, s1, s2 = [0] * n, [0] * n, [], []

        # (*)
        for i in range(n):
            count = 1
            while s1 and s1[-1][0] > A[i]:
                count += s1.pop()[1]
            left[i] = count
            s1.append([A[i], count])

        # (**)
        for i in range(n)[::-1]:
            count = 1
            while s2 and s2[-1][0] >= A[i]:
                count += s2.pop()[1]
            right[i] = count
            s2.append([A[i], count])

        return sum(a * l * r for a, l, r in zip(A, left, right)) % mod

    # Mine...
    def sumSubarrayMins(self, A: List[int]) -> int:
        sum_so_far = 0
        non_dec_stack = []
        for idx, item in enumerate(A, 1):
            while non_dec_stack and non_dec_stack[-1][0] > item:
                pop_item, pop_idx = non_dec_stack.pop()

                left_idx = non_dec_stack[-1][1] if non_dec_stack else 0
                left_distance = pop_idx - left_idx
                right_distance = idx - pop_idx

                sum_so_far += left_distance * right_distance * pop_item

            non_dec_stack.append([item, idx])

        while non_dec_stack:
            pop_item, pop_idx = non_dec_stack.pop()

            left_idx = non_dec_stack[-1][1] if non_dec_stack else 0
            left_distance = pop_idx - left_idx
            right_distance = len(A) + 1 - pop_idx

            sum_so_far += left_distance * right_distance * pop_item

        return sum_so_far % (10 ** 9 + 7)






















































