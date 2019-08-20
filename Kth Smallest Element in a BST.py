class Solution:

	def __init__(self):
		self.counter = 0
		self.result = 0

	def kthSmallestElement(self, root: 'TreeNode', k: int) -> int:
		if root.left:
			kthSmallestElement(root.left, k)
		#Recurse until the leftmost element. First check each node's left child.
		self.counter += 1
		#Rank the elements from 1.
		if self.counter == k:
			self.result = root.val
		#When the counter reaches k, the kth element is found.
		if root.right:
			kthSmallestElement(root.right, k)
		#Then check each node's right child.
		return self.result