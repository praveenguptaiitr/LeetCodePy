# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if root is None:
            return []

        ans = []
        q = []
        q.append(root)
        tmp = root
        while len(q) > 0:
            #tmp = q[-1]
            while tmp is not None and tmp.left is not None:
               q.append(tmp.left)
               tmp = tmp.left
            tmp = q.pop()
            ans.append(tmp.val)
            if tmp.right is not None:
                q.append(tmp.right)
            tmp = tmp.right

        return ans


if __name__ == "__main__":
    s = Solution()
    t = TreeNode(5)
    #t.left = TreeNode(3)
    #t.left.right = TreeNode(4)
    t.right = TreeNode(20)
    t.right.right = TreeNode(25)
    print(s.inorderTraversal(t))
