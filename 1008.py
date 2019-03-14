# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if preorder == None:
            return None
        if len(preorder)==0:
            return None

        root = TreeNode(preorder[0])
        if len(preorder)==1:
            return root
        if len(preorder)==2:
            if preorder[1]>root.val:
                root.right = TreeNode(preorder[1])
            else:
                root.left = TreeNode(preorder[1])
            return root

        idex = -1
        for i in range(1, len(preorder)):
            if preorder[i]>root.val:
                idex=i
                break

        if idex == 1:
            root.left = None
            root.right = self.bstFromPreorder(preorder[1:])
            return root
        if (idex == -1) :
            root.right = None
            root.left = self.bstFromPreorder(preorder[1:])
            return root
        root.left = self.bstFromPreorder(preorder[1:idex])
        root.right = self.bstFromPreorder(preorder[idex:])
        return root

if __name__ == "__main__":
    s = Solution()

    t = s.bstFromPreorder([3,1,2])
    print(t)