# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
            self.ans = float("Inf")
            self.prev = None

    def dfs(self, root):
            if root is None:
                return

            #prev = root
            self.dfs(root.left)
            if self.prev is not None:
                self.ans = min(abs(root.val - self.prev.val), self.ans)
            self.prev = root
            self.dfs(root.right)

            return

    def minDiffInBST(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """

            if root is None:
                return 0

            prev = None
            self.dfs(root)
            return self.ans


if __name__ == "__main__":
    s = Solution()
    t = TreeNode(27)
    t.right = TreeNode(34)
    t.right.right = TreeNode(58)
    t.right.right.left = TreeNode(50)
    t.right.right.left.left = TreeNode(44)
    print(s.minDiffInBST(t))