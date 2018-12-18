# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.ans = [float('Inf')]*2

    def dfs(self,root):
        if root is None:
            return

        self.dfs(root.left)
        if root.val != self.ans[0] and root.val!=self.ans[1]:
            if root.val<=self.ans[0]:
                self.ans.pop(1)
                self.ans.insert(0,root.val)
            elif root.val>= self.ans[0] and root.val< self.ans[1]:
                self.ans.pop(1)
                self.ans.append(root.val)

        self.dfs(root.right)


    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root)
        if self.ans[0]==float('Inf') or self.ans[1]==float('Inf'):
            return -1

        if self.ans[0] == self.ans[1]:
            return -1

        return self.ans[1]




if __name__=="__main__":
    s= Solution()
    t = TreeNode(2)
    t.left = TreeNode(2)
    t.right = TreeNode(5)
    t.right.left = TreeNode(5)
    t.right.right= TreeNode(7)
    print(s.findSecondMinimumValue(t))