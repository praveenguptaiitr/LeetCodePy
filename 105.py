# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.k = -1

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder)==0:
            return None

        self.k += 1

        if len(inorder)==1:
            t = TreeNode(inorder[0])
            return t

        m = inorder.index(preorder[self.k])
        t = TreeNode(preorder[m])
        t.left = self.buildTree(preorder,inorder[:m])
        t.right= self.buildTree(preorder,inorder[m+1:])
        return t

if __name__=='__main__':
    s = Solution()

