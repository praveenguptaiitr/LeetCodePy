# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def __init__(self):
        self.arr = []
        self.idx = 0

    def ser(self, root):
        if root is not None:
            k = str(root.val)
            self.arr.append(k)
            self.ser(root.left)
            self.ser(root.right)
        else:
            self.arr.append("#")

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.ser(root)
        ans = " ".join(self.arr)
        self.arr = []
        return ans


    def dser(self, l):
        if(self.idx <= len(l)):
            if l[self.idx]=="#":
                return None
            else:
                t = TreeNode(l[self.idx])
                self.idx+=1
                t.left = self.dser(l)
                self.idx+=1
                t.right = self.dser(l)
                return t
        else:
            return None


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        l = data.split()
        n = len(l)

        t= self.dser(l)
        self.idx=0
        return t

t = TreeNode(2)
t.left = TreeNode(1)
t.right = TreeNode(3)

# Your Codec object will be instantiated and called as such:
codec = Codec()
codec.deserialize(codec.serialize(t))
#print(codec.serialize(t))