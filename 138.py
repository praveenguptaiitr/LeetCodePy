# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def printNone(self, head, c = "-"):
        print(c*5)
        while(head is not None):
            print(head.label)
            head=head.next
        print(c * 5)

    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        if head is None:
            return None


        tmp = head
        while tmp is not None:
            t = RandomListNode(tmp.label)
            t.next = tmp.next
            tmp.next = t
            tmp = t.next

        tmp = head
        while tmp is not None:
            if tmp.random is not None:
                tmp.next.random = tmp.random.next
            tmp = tmp.next.next

        l1 = head
        l2 = head.next
        h1 = l2

        while l1 is not None:
            l1.next = l1.next.next
            if l2.next is not None:
                l2.next = l2.next.next
            l1 = l1.next
            l2=l2.next

        return h1

if __name__ == "__main__":
    s = Solution()
    l = RandomListNode(1)
    l.next = RandomListNode(2)
    l.next.next = RandomListNode(3)
    l.next.next.next = RandomListNode(4)
    l.next.next.next.next = RandomListNode(5)

    s.copyRandomList(l)