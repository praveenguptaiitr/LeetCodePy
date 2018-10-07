# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getValue(self, root):
        if root == None:
            return 0
        l = 0
        r = 0
        if root.left is not None:
            l = self.getValue(root.left)
            if l == 0:
                root.left = None

        if root.right is not None:
            r = self.getValue(root.right)
            if r ==0:
                root.right = None

        if (root.val + l + r)==0:
            return 0
        else:
            return 1


    def pruneTree(self, root):
        """
        :type root: TreeNodeif
        :rtype: TreeNode
        """
        if root == None:
            return root

        if root.left is not None and self.getValue(root.left)==0:
            root.left = None
        if root.right is not None and self.getValue(root.right)==0:
            root.right= None
        return root





if __name__ == "__main__":
    s = Solution()

    s.pruneTree(node)