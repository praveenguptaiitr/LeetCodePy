from random import randrange


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        l = 0
        curr = head
        while (curr is not None):
            curr = curr.next
            l += 1
        self.len = l

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        r = randrange(self.len)
        if r == 0:
            return self.head.val

        k = 0

        curr = self.head

        while (k < r):
            curr = curr.next
            k += 1
        return curr.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()