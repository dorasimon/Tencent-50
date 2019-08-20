"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

	def __init__(self):
		self.counter = 0
		self.result = 0

	def kthSmallest(self, root: TreeNode, k: int) -> int:
		if root.left:
			self.kthSmallest(root.left, k)
		#Recurse until the leftmost element. First check each node's left child.
		self.counter += 1
		#Rank the elements from 1.
		if self.counter == k:
			self.result = root.val
		#When the counter reaches k, the kth element is found.
		if root.right:
			self.kthSmallest(root.right, k)
		#Then check each node's right child.
		return self.result