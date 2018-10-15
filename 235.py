# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None

        elif p is None and q is not None:
            return q

        elif q is None and p is not None:
            return p

        elif root == q and root != p:
            return q

        elif root == p and root != q:
            return p

        elif (root is not None and q is not None and p is not None) and (root.val > q.val and root.val > p.val):
            return self.lowestCommonAncestor(root.left, p, q)

        elif (root is not None and q is not None and p is not None) and (root.val < q.val and root.val < p.val):
            return self.lowestCommonAncestor(root.right, p, q)

        return root




