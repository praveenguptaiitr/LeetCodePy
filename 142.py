# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return None
        if head.next is None:
            return None

        slow = head
        fast = head.next
        meet = None

        while fast is not None and fast.next is not None:
            if slow == fast:
                meet = slow
                break
            else:
                slow = slow.next
                fast = fast.next.next

        if fast is None or fast.next is None:
            return None

        slow=slow.next

        tmp = head
        while tmp != slow:
            tmp = tmp.next
            slow = slow.next

        return tmp

if __name__ =="__main__":
    s = Solution()
    l = ListNode(3)
    l.next=ListNode(2)
    l.next.next = ListNode(0)
    l.next.next.next = ListNode(-4)
    l.next.next.next.next = l.next
    print(s.detectCycle(l))