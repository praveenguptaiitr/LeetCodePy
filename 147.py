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

    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return None

        if head.next is None:
            return head

        if head.next.next is None:
            if head.val > head.next.val:
                head.next.next = head
                t = head.next
                head.next = None
                return t
            else:
                return head


        start = head
        end = head
        curr = end.next
        while(curr is not None):
            if curr.val > end.val:
                end = curr
                curr=curr.next
            elif curr.val <= start.val:
                end.next = curr.next
                curr.next = start
                start = curr
                curr=end.next
            else:
                tmp = start
                prev = None
                while tmp.val<curr.val:
                    prev = tmp
                    tmp=tmp.next
                end.next = curr.next
                curr.next = prev.next
                prev.next = curr
                curr=end.next

        print("---------")
        self.printNone(start)
        print("---------")
        return start

if __name__=="__main__":
    s = Solution()
    # l = ListNode(4)
    # l.next = ListNode(2)
    # l.next.next = ListNode(1)
    # l.next.next.next = ListNode(3)
    # s.insertionSortList(l)

    l = ListNode(0)
    l.next = ListNode(0)
    l.next.next = ListNode(0)
    l.next.next.next = ListNode(0)
    s.insertionSortList(l)