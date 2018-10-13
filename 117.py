# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is None:
            return

        parent = None
        child = None
        childHd = None
        parent = root
        while parent is not None:
            while parent is not None:
                if parent.left is not None:
                    if childHd is None:
                        childHd = parent.left
                    else:
                        child.next = parent.left
                    child = parent.left

                if parent.right is not None:
                    if childHd is None:
                        childHd = parent.right
                    else:
                        child.next = parent.right
                    child = parent.right

                parent = parent.next

            parent = childHd
            childHd = None
            child = None





if __name__=="__main__":
    s = Solution()
    l = TreeLinkNode(1)
    l.left=TreeLinkNode(2)
    l.right=TreeLinkNode(3)
    # l.left.left=TreeLinkNode(4)
    # l.left.right=TreeLinkNode(5)
    # l.right.right=TreeLinkNode(6)
    # l.left.left.left = TreeLinkNode(7)
    # l.right.right.right = TreeLinkNode(8)
    s.connect(l)