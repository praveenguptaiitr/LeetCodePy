# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def traverse(self, root, l, depth):
        if root is None:
            return l
        if len(l)-1 >= depth:
            l.append(root.val)
        self.traverse(root.left,l,depth+1)
        l[depth] = root.val
        self.traverse(root.right, l, depth+1)

        return

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        l = []
        self.traverse(root,l,0)
        return l

#if __name__=='__main__':
#    s = Solution()
#    s.rightSideView()