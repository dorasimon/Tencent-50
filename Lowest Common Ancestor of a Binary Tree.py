"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

	def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
		def recurseTree(node) -> bool:
			if not node:
				return False
			#If it exceeds the leaf node, return False.
			left = recurseTree(node.left)
			right = recurseTree(node.right)
			#Recurse both directions.
			itself = node == p or node == q
			#If it reaches p or q, mark it.
			if left + right + itself >= 2:
				self.result = node
			return left or right or itself
			#When both subtrees return True or one subtree and itself return True, the node is the LCA.
		recurseTree(root)
		return self.result