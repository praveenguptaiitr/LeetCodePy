# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def printNone(self, head):
        while(head is not None):
            print(head.val)
            head=head.next


    def merge(self, l1, l2):
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        m1 = l1
        m2 = l2
        m3 = None

        if m1.val < m2.val:
            m3 = m1
            m1 = m1.next
        else:
            m3= m2
            m2 = m2.next
        head = m3
        while (m1 is not None and m2 is not None):
            if m1.val<m2.val:
                m3.next = m1
                m1 = m1.next
            else:
                m3.next = m2
                m2 = m2.next
            m3=m3.next

        if m1 is None and m2 is not None:
            while(m2 is not None):
                m3.next = m2
                m2 = m2.next
                m3 = m3.next

        if m2 is None and m1 is not None:
            while(m1 is not None):
                m3.next = m1
                m1 = m1.next
                m3 = m3.next

        return head

    def msort(self, head):
        if head is None:
            return None

        if head.next is None:
            return head

        slow = head
        fast = head
        mid = None
        prev = None

        while(fast is not None and fast.next is not None):
            prev = slow
            slow = slow.next
            fast = fast.next.next

        mid = slow
        prev.next = None
        l1 = self.msort(head)
        l2 = self.msort(mid)

        l3 = self.merge(l1,l2)
        return l3


    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return None

        if head.next is None:
            return head

        x = self.msort(head)
        #print("++++")
        self.printNone(x)
        return x

if __name__ =="__main__":
    s = Solution()
    l = ListNode(3)
    l.next = ListNode(1)
    l.next.next = ListNode(8)
    l.next.next.next = ListNode(2)
    l.next.next.next.next = ListNode(0)

    s.sortList(l)
