class Solution:
    def __init__(self):
        self.sum = 0

    def sumL(self, root, parent):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0

        if root.left is None and root.right is None and parent.left == root:
            return root.val

        l1 = 0
        l2= 0
        if root.left is not None:
            l1 = self.sumL(root.left, root)
        if root.right is not None:
            l2 = self.sumL(root.right, root)
        return l1+l2

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 0

        return self.sumL(root.left, root)+self.sumL(root.right, root)