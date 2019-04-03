# 496. Next Greater Element I
#
# You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2.
# Find all the next greater numbers for nums1's elements in the corresponding places of nums2.
#
# The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2.
# If it does not exist, output -1 for this number.

# 질문 자체가 구릴 수 밖에 없음... nums2에서 엘리멘트i보다 큰 숫자가 오른쪽에 존재하면 그 숫자를 반환해라 이거임...
#
# Example 1:
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
# Output: [-1,3,-1]
# Explanation:
#     For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
#     For number 1 in the first array, the next greater number for it in the second array is 3.
#     For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
# Example 2:
# Input: nums1 = [2,4], nums2 = [1,2,3,4].
# Output: [3,-1]
# Explanation:
#     For number 2 in the first array, the next greater number for it in the second array is 3.
#     For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
'''
nums2 = [2, 0, -1, 1, 4]

Keep monotonic decreasing stack
[2]
[2, 0]
[2, 0, -1]
[2, 1]
[4]
'''


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # lets keep a monotonic decreasing stack
        stack = []

        get_num2_by_key = {item: idx for idx, item in enumerate(nums2)}

        next_greater_elem = [-1] * len(nums2)
        for idx, item in enumerate(nums2):
            while stack and stack[-1][1] < item:
                pop_idx, pop_elem = stack.pop()
                next_greater_elem[pop_idx] = item
            stack.append([idx, item])

        return [next_greater_elem[get_num2_by_key[key]] for key in nums1]






