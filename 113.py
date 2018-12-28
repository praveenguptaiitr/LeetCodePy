# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.ans = []

    def dfs(self, root, sum, path):
        if root is None:
            return

        path.append(root.val)
        sum = sum-root.val
        self.dfs(root.left, sum, path)

        if root.left is None and root.right is None:
            if sum ==0:
                p = path[:]
                self.ans.append(p)
                path.pop()
                return
            else:
                sum += root.val
                path.pop()
                return

        self.dfs(root.right, sum, path)
        path.pop()

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        if root is None and sum == 0:
            return []
        if root.left is None and root.right is None and sum == root.val:
            return [[root.val]]

        path = list()
        self.dfs(root, sum, path)
        return self.ans

if __name__=="__main__":
    s = Solution()
    t = TreeNode(5)
    t.left = TreeNode(4)
    t.right = TreeNode(8)
    t.left.left = TreeNode(11)
    t.left.left.left = TreeNode(7)
    t.left.left.right = TreeNode(2)
    t.right.left = TreeNode(13)
    t.right.right = TreeNode(4)
    t.right.right.left = TreeNode(5)
    t.right.right.right = TreeNode(1)
    s.pathSum(t,22)
