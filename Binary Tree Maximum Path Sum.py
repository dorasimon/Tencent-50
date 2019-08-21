"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-maximum-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

	def maxPath(self, root: TreeNode) -> int:
		if not Node:
			return 0
		left = self.maxPath(Node.left)
		right = self.maxPath(Node.right)
		maxBranchValue = max(left, right) + Node.val
		self.max = max(left + right + Node.val, self.max)
		if maxBranchValue > 0:
			return maxBranchValue
		else:
			return 0

	def maxPathSum(self, root: TreeNode) -> int:
		self.max = float('-inf')
		self.maxPath(root)
		return self.max