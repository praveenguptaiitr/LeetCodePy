# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def __init__(self):
        self.d = {}

    def dfs(self, root):
        if root is None:
            return float("-inf")

        ans = 0
        l = self.dfs(root.left)
        r = self.dfs(root.right)

        if l != float("-inf"):
            ans+=l
        if r != float("-inf"):
            ans+=r

        ans +=root.val

        self.d[ans] = self.d.get(ans,0)+1
        return ans


    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if root is None:
            return []

        self.dfs(root)
        m = max(self.d.values())
        ans = []
        for k,v in self.d.items():
            if v == m:
                ans.append(k)
        return ans


