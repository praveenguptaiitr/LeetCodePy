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

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1 is None and l2 is not None:
            return l2

        if l2 is None and l1 is not None:
            return l1

        carry = 0
        t = l1.val + l2.val
        if t > 9:
            carry=1
            t = t%10
        l3 = ListNode(t)
        head = l3
        l1 = l1.next
        l2 = l2.next
        while l1 is not None and l2 is not None:
            t = l1.val+l2.val+carry
            if t > 9 :
                t  = t%10
                carry=1
            else:
                carry=0
            l3.next = ListNode(t)
            l3 = l3.next
            l1 = l1.next
            l2 = l2.next

        if l1 is None:
            while(l2 is not None):
                t = l2.val+carry
                if t > 9:
                    carry=1
                    t = t%10
                else:
                    carry=0
                l3.next = ListNode(t)
                l3 = l3.next
                l2 =l2.next

        if l2 is None:
            while(l1 is not None):
                t = l1.val+carry
                if t > 9:
                    carry=1
                    t = t%10
                else:
                    carry=0
                l3.next = ListNode(t)
                l3 = l3.next
                l1 =l1.next

        if carry == 1:
            l3.next = ListNode(1)

        self.printNone(head)
        return head

if __name__ =="__main__":
    s = Solution()
    l1 = ListNode(1)
    # l1.next = ListNode(4)
    # l1.next.next = ListNode(3)

    l2 = ListNode(9)
    l2.next = ListNode(9)
    # l2.next.next = ListNode(4)

    s.addTwoNumbers(l1,l2)