# 206. Reverse Linked List
# Reverse a singly linked list.
#
# Example:
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:
#
# A linked list can be reversed either iteratively or recursively. Could you implement both?


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        dummy_head = ListNode(None)
        dummy_head.next = temp = head

        while temp and temp.next:
            next_node = temp.next
            next_node.next, temp.next, dummy_head.next = (dummy_head.next,
                                                          next_node.next,
                                                          next_node)

        return dummy_head.next

    '''
         1 -> 2 -> 3 -> x
    x <- 1 <- 2 <- 3
    '''
    def reverseListFromDiscussion(self, head: ListNode) -> ListNode:
        cur, prev = head, None
        while cur:
            cur, prev, cur.next = cur.next, cur, prev
        return prev

    def reverseListAnother(self, head):
        if not head or not head.next:
            return head
        new_head = self.reverseListAnother(head.next)
        last_node = new_head
        while last_node and last_node.next:
            last_node = last_node.next
        last_node.next = head
        head.next = None
        return new_head


if __name__ == '__main__':
    s = Solution()
    given = [ListNode(i) for i in range(5)]
    for idx, node in enumerate(given):
        if idx < len(given)-1:
            node.next = given[idx+1]
            print(node.val)
    reverse_head = s.reverseListAnother(given[0])
    while reverse_head:
        print(reverse_head.val)
        reverse_head = reverse_head.next




