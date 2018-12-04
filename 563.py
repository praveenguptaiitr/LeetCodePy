# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.ans = 0

    def helper(self, root):
        if root is None:
            return 0

        l = self.helper(root.left)
        r = self.helper(root.right)
        self.ans += abs(l-r)

        return root.val + l+r

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        self.helper(root)

        return self.ans

if __name__ == "__main__":

    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(3)

    s = Solution()
    print(s.findTilt(t))