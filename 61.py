# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def printNode(self, head):
        while(head is not None):
            print(head.val)
            head=head.next

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if head is None:
            return None

        if head.next is None or k==0:
            return head

        l = 0
        c = head
        while c is not None:
            c=c.next
            l+=1

        k=k%l
        curr = head
        prev = None
        while k > 0:
            while curr.next is not None:
                prev = curr
                curr = curr.next

            prev.next = None
            curr.next = head
            head = curr
            k-=1

        print("----------")
        self.printNode(head)
        print("----------")
        return head

if __name__=="__main__":
    s = Solution()
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(4)
    l.next.next.next.next = ListNode(5)

    s.rotateRight(l, 2)
