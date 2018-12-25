# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def func(self, head):
        if head is None:
            return None

        if head.next is None:
            return TreeNode(head.val)

        mid = None
        slow = head
        fast = head
        prev = None
        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        mid = slow
        prev.next = None

        t = TreeNode(mid.val)
        t.left = self.func(head)
        t.right = self.func(mid.next)
        return t

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        if head is None:
            return None

        if head.next is None:
            return TreeNode(head.val)

        return self.func(head)