"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def __init__(self):
        self.ans = []

    def traverse(self, root):
        if root is None:
            return

        for r in root.children:
            self.traverse(r)

        self.ans.append(root.val)
        return

    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []

        self.traverse(root)
        return self.ans