# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def print(self, root):
        if root is None:
            return
        self.print(root.left)
        print(root.val)
        self.print(root.right)


    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """

        if root is None:
            return None

        curr = root
        prev = None

        if root.val == key and root.left is None and root.right is None:
            return None

        while curr is not None and curr.val != key:
            if curr.val>key:
                prev = curr
                curr = curr.left
            else:
                prev=curr
                curr=curr.right

        if curr is None:
            return root

        if curr.left is None and curr.right is None:
            if prev is None:
                return None

            if prev.left is curr:
                prev.left = None
            else:
                prev.right = None

        if curr.left is None and curr.right is not None:
            if prev is None:
                root = curr.right
                return root

            if prev.left is curr:
                prev.left = curr.right
            else:
                prev.right = curr.right

        if curr.right is None and curr.left is not None:
            if prev is None:
                root = curr.left
                return root

            if prev.left is curr:
                prev.left = curr.left
            else:
                prev.right = curr.left


        if curr.left is not None and curr.right is not None:
            tmp = curr.right
            prev = curr
            while(tmp.left is not None):
                prev = tmp
                tmp = tmp.left
            curr.val = tmp.val
            if prev.left is tmp:
                prev.left = tmp.right
            else:
                prev.right = tmp.right


        return root

if __name__=="__main__":
    s = Solution()
    t = TreeNode(5)
    t.left = TreeNode(3)
    t.right = TreeNode(6)
    t.left.left = TreeNode(2)
    t.left.right = TreeNode(4)
    t.right.right = TreeNode(7)

    x = s.deleteNode(t,5)
    s.print(x)