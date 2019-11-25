# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        curr = head
        count = 0
        while curr is not None:
            count += 1
            curr = curr.next
        iters = count // k
        dummy = ListNode(float("-inf"))
        dummy.next = head
        curr = head
        prev = dummy

        for _ in range(iters):
            temp1 = None
            for _ in range(k - 1):
                temp1 = curr.next
                curr.next = temp1.next
                temp1.next = prev.next
                prev.next = temp1

            prev = curr
            curr = curr.next

        return dummy.next

if __name__ =="__main__":
    s = Solution()
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(4)
    # l.next.next.next.next = ListNode(5)
    # l.next.next.next.next.next = ListNode(6)
    # l.next.next.next.next.next.next = ListNode(7)
    # l.next.next.next.next.next.next.next = ListNode(8)
    k = s.reverseKGroup(l,4)
    s.printl(k)
