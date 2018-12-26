# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """

        if len(pre)<= 0:
            return None
        if len(pre)==1:
            return TreeNode(pre[0])

        t = TreeNode(pre[0])
        l = post.index(pre[1])+1
        t.left = self.constructFromPrePost(pre[1:l+1],post[0:l])
        t.right = self.constructFromPrePost(pre[l+1:],post[l:])
        return t
