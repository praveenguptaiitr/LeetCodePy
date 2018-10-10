# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        if head.next is None:
            return head

        if head.next.next is None:
            return head

        odd = head
        even = head.next
        temp1= odd
        temp2 = even

        while odd is not None and even is not None:
            podd=odd
            odd.next = even.next
            odd=odd.next
            if odd is not None:
                even.next = odd.next
                even=even.next

        if odd is not None :
            odd.next = temp2
        if odd is None:
            podd.next = temp2

        return head