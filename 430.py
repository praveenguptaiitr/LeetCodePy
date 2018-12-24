
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child



class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        if head is None:
            return None

        curr = head
        while curr is not None:
            if curr.child is not None:
                t = curr.next
                curr.next = curr.child
                tmp = curr.next
                curr.child = None
                curr.next.prev = curr
                while tmp.next is not None:
                    tmp = tmp.next
                tmp.next = t
                if t is not None:
                    t.prev = tmp
            curr = curr.next

        return head



