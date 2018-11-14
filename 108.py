# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	def sortedArrayToBST(self, nums):
		"""
		:type nums: List[int]
		:rtype: TreeNode
		"""

		if len(nums)==0:
			return None
		return self.arr2tree(nums)


	def arr2tree(self,nums):

		if len(nums)==0:
			return None

		mid = int(len(nums)/2)
		t = TreeNode(nums[mid])
		t.left =self.arr2tree(nums[:mid])
		t.right = self.arr2tree(nums[mid+1:])

		return t
