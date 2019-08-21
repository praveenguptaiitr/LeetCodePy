# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.ans = float("-inf")

    def helper(self, root):
        if root is None:
            return float("-inf")


        l = self.helper(root.left)
        r = self.helper(root.right)

        v = max(root.val,max(l+root.val, r+ root.val))

        self.ans = max(self.ans, max(v, root.val+l+r) )

        return v

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.helper(root)
        return self.ans


if __name__ == "__main__":
    t = TreeNode(1)
    t.left = TreeNode(-2)
    t.right = TreeNode(3)
    s = Solution()
    print(s.maxPathSum(t))