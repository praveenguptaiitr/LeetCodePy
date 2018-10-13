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

    def connectNext(self,root,next):
        if root is None:
            return



        root.next = next

        if root.left is not None:
            self.connectNext(root.left, root.right)

        if root.right is not None:
            if root.next is not None:
                self.connectNext(root.right,root.next.left)
            else:
                self.connectNext(root.right, None)
        return


    def connect(self, root):
        if root is None:
            return
        else:
            self.connectNext(root,None)
            return

if __name__=="__main__":
    s = Solution()
    l = TreeLinkNode(1)
    l.left=TreeLinkNode(2)
    l.right=TreeLinkNode(3)
    # l.left.left=TreeLinkNode(4)
    # l.left.right=TreeLinkNode(5)
    # l.right.left=TreeLinkNode(6)
    # l.right.right=TreeLinkNode(7)
    s.connect(l)