from collections import defaultdict
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        frontier = []
        frontier.append(root)
        level = [] #defaultdict(list)
        depth = 0
        ans = []
        val = []
        val.append(root.val)
        while frontier:
            level.append(frontier)
            ans.append(val)
            next = []
            val = []
            for u in frontier:
                if u.left is not None:
                    next.append(u.left)
                    val.append(u.left.val)
                if u.right is not None:
                    next.append(u.right)
                    val.append(u.right.val)
            depth +=1
            frontier=next
        ans.reverse()
        return ans


if __name__=='__main__':
  t = TreeNode(3)
  t.left=TreeNode(9)
  t.right=TreeNode(20)
  t.right.left=TreeNode(15)
  t.right.right=TreeNode(7)
  s = Solution()
  k = s.levelOrderBottom(t)
  print(k)