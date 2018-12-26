# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.first = False
        self.parent = []
        self.curr = None
        tmp = root
        while(tmp.left is not None):
            self.parent.append(tmp)
            tmp = tmp.left

        self.curr = tmp


    def hasNext(self):
        """
        :rtype: bool
        """
        if self.curr is None:
            return False
        if self.curr.right is not None:
            return True
        p = self.parent[:]
        k = self.curr
        while len(p)>0:
            n = p.pop()
            if n.left == k:
                return True
            k = n
        if len(p)==0:
            return False

    def next(self):
        """
        :rtype: int
        """
        if self.curr is not None and self.first is False:
            self.first = True
            return self.curr.val
        if self.curr.right is not None:
            self.parent.append(self.curr)
            tmp = self.curr.right
            self.parent.append(self.curr)
            while(tmp.left is not None):
                self.parent.append(tmp)
                tmp = tmp.left
            self.curr = tmp
            return self.curr.val

        p = self.parent[:]
        k = self.curr
        while len(p)>0:
            n = p.pop()
            if n.left == k:
                self.curr = n
                self.parent = p[:]
                return self.curr.val
            k = n
        if len(p)==0:
            self.curr = None
            return None


# Your BSTIterator will be called like this:
t = TreeNode(10)
t.left = TreeNode(5)
t.left.left = TreeNode(4)
t.left.right = TreeNode(6)
t.right = TreeNode(15)

i, v = BSTIterator(t), []
while i.hasNext():
    v.append(i.next())
    print(v[-1])
