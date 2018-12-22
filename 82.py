# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        dummy = ListNode(float('-Inf'))
        dummy.next = head
        pre = dummy
        cur = head
        while cur is not None and cur.next is not None:
            num = cur.val
            if cur.val == cur.next.val:
                while cur and cur.val == num:
                    cur = cur.next
                pre.next = cur
            else:
                pre = cur
                cur = cur.next

        return dummy.next

if __name__=="__main__":
    s = Solution()
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(3)
    l.next.next.next.next = ListNode(4)
    l.next.next.next.next.next = ListNode(4)
    l.next.next.next.next.next.next = ListNode(5)
    s.deleteDuplicates(l)

    # l = ListNode(1)
    # l.next = ListNode(1)
    # l.next.next = ListNode(2)
    # l.next.next.next = ListNode(2)
    #l.next.next.next.next = ListNode(3)
    s.deleteDuplicates(l)
