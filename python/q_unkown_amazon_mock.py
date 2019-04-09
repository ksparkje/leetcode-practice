# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def check_bst(node, min, max):
            if not node:
                return True
            if not min <= node.val <= max:
                return False
            return (check_bst(node.left, min, node.val) and
                    check_bst(node.right, node.val, max))

        inf = float('inf')
        return check_bst(root, -inf, inf)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        dummy_node = cur_head = ListNode(-1)
        carry = 0

        while l1 or l2 or carry:

            if not (l1 or l2):
                # carry is the only value
                cur_val = carry
                carry = 0

            else:
                if l1:
                    l1_val = l1.val
                    l1 = l1.next
                else:
                    l1_val = 0

                if l2:
                    l2_val = l2.val
                    l2 = l2.next
                else:
                    l2_val = 0

                cur_val = l1_val + l2_val + carry
                carry = cur_val // 10
                cur_val %= 10

            cur_head.next = ListNode(cur_val)
            cur_head = cur_head.next

        return dummy_node.next


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = right = 1
        result = [1] * len(nums)

        for idx in range(len(nums)):
            result[idx] *= left
            left *= nums[idx]
            result[~idx] *= right
            right *= nums[~idx]
        return result


# Check two binary trees leaves are equal when one is reversed


# Return the sum of left leaves / sum of right leaves







