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

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        if head is None:
            return None

        if head.next is None and n==1:
            return None

        i=1
        curr = head
        while(i<=n):
            curr=curr.next
            i+=1

        if curr is None :
            head = head.next
            return head


        prev = head
        while(curr.next is not None):
            prev = prev.next
            curr= curr.next

        prev.next = prev.next.next
        print("---------")
        self.printNone(head)
        print("---------")

        return head

if __name__=="__main__":
    s = Solution()
    l = ListNode(1)
    l.next = ListNode(2)
    # l.next.next = ListNode(3)
    # l.next.next.next = ListNode(4)
    # l.next.next.next.next = ListNode(5)
    s.removeNthFromEnd(l,1)
