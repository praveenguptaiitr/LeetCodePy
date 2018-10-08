# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def construct(self, nums):
        if len(nums)==0:
            return None
        if len(nums)==1:
            t = TreeNode(nums[0])
            return t


        cut = nums.index(max(nums))
        t = TreeNode(max(nums))
        t.left = self.construct(nums[0:cut])
        t.right = self.construct(nums[cut+1:])
        return t


    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) ==0:
            return None
        else:
            return self.construct(nums)




if __name__ == '__main__':
    s = Solution()
    s.constructMaximumBinaryTree([3,2,1,6,0,5])