# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head is None:
            return None

        if m == n:
            return head

        dummy_head = ListNode(float("-inf"))
        dummy_head.next = head
        curr = head
        prev = dummy_head
        count = 1
        while count < m:
            prev = curr
            curr = curr.next
            count += 1

        temp1 = None
        for _ in range(n - m):
            temp1 = curr.next
            curr.next = temp1.next
            temp1.next = prev.next
            prev.next = temp1

        return dummy_head.next

if __name__=="__main__":
    s = Solution()
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(4)
    l.next.next.next.next = ListNode(5)

    s.reverseBetween(l,2,4)
