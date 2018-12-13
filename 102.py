# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root is None:
            return []

        ans = []
        ans.append(root.val)
        frontier = []
        frontier.append(root)

        next = []
        l = []
        while len(frontier) > 0:
            while len(frontier) > 0:
                e = frontier[0]
                del frontier[0]

                if e.left is not None:
                    next.append(e.left)
                    l.append(e.left.val)
                if e.right is not None:
                    next.append(e.right)
                    l.append(e.right.val)
            if len(l) > 0:
                ans.append(l)
            frontier = next
            next = []
            l = []

        return ans


if __name__ == "__main__":
    s = Solution()
    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(3)
    t.left.left = TreeNode(4)
    t.left.right = TreeNode(5)
    print(s.levelOrder(t))