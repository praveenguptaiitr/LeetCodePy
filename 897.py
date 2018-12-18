# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.head = None
        self.curr = None

    def createTree(self, root):
        if root is None:
            return

        self.createTree(root.left)
        if self.head is None:
            self.head = TreeNode(root.val)
            self.curr = self.head
        else:
            self.curr.right = TreeNode(root.val)
            self.curr = self.curr.right
        self.createTree(root.right)




    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if root is None:
            return root

        self.createTree(root)
        return self.head



if __name__ =="__main__":
    s = Solution()
    t = TreeNode(3)
    t.right = TreeNode(5)
    k = s.increasingBST(t)
    print(k)

