# 19. Remove Nth Node From End of List

# Given a linked list, remove the n-th node from the end of list and return its head.
# 
# Example:
# 
# Given linked list: 1->2->3->4->5, and n = 2.
# 
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
# 
# Given n will always be valid.
# 
# Follow up:
# 
# Could you do this in one pass?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        total_len = self._get_length_of_list(head)        
        if total_len < n:
            return head

        dummy_head = ListNode(-1)
        dummy_head.next = head

        jumped = non_jumped = dummy_head
        
        for _ in range(n):
            jumped = jumped.next
        
        while jumped and jumped.next:
            jumped = jumped.next
            non_jumped = non_jumped.next
    
        non_jumped.next = None if not jumped else non_jumped.next.next

        return dummy_head.next

    def _get_length_of_list(self, node):
        temp = node
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count
            
