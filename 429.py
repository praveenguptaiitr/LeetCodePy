"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        ans = []
        frontier = []
        next1 = []
        next2 = [root.val]
        frontier.append(root)
        # print("1")
        ans.append(next2)
        next2 = []
        while (len(frontier) != 0):
            for n in frontier:
                if len(n.children) > 0:
                    for c in n.children:
                        # print(c.val)
                        next1.append(c)
                        next2.append(c.val)
            # print("3")
            if len(next2) > 0:
                ans.append(next2)
            frontier = next1
            next1 = []
            next2 = []
            # print("level change")

        return ans