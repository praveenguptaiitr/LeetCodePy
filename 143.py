# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def printNone(self, head, c="-"):
        print(c*5)
        while(head is not None):
            print(head.val)
            head=head.next
        print(c * 5)

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None:
            return None
        if head.next is None:
            return
        if head.next.next is None:
            return

        curr = head
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        l2 = slow.next
        slow.next = None
        l1 = head
        # self.printNone(l1)
        # self.printNone(l2,"+")

        if l2.next is not None:
            prev = None
            mid = l2
            front = l2.next
            while(front is not None):
                mid.next = prev
                prev = mid
                mid = front
                front = front.next
            mid.next = prev

            l2 = mid
            #self.printNone(l2,"=")

        tmp1 = l1
        tmp2 = l2
        while tmp2 is not None:
            t = tmp1.next
            tmp1.next=tmp2
            tmp2 = tmp2.next
            tmp1.next.next = t
            tmp1 = t

        #self.printNone(l1)
        #return l1



if __name__=="__main__":
    s = Solution()
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(4)
    l.next.next.next.next = ListNode(5)
    s.reorderList(l)
