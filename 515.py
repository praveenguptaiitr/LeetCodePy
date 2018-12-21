# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        frontier = []
        next = []
        v = []
        ans = []
        ans.append(root.val)
        frontier.append(root)

        while len(frontier)>0:
            next = []
            v = []
            while len(frontier)>0:
                e = frontier.pop()
                if e.left is not None:
                    next.append(e.left)
                    v.append(e.left.val)
                if e.right is not None:
                    next.append(e.right)
                    v.append(e.right.val)

            frontier = next
            if len(next)>0:
                ans.append(max(v))
        return ans

if __name__ == "__main__":
    s = Solution()
    t = TreeNode(5)
    t.left = TreeNode(14)
    t.left.left = TreeNode(1)


    print(s.largestValues(t))