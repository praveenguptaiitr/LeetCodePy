# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None :
            return None

        if head.next is None:
            return head

        t1 = head.next
        #t2 = head.next.next

        nl = self.swapPairs(t1.next)

        t1.next = head
        head.next = nl
        head = t1

        return head

