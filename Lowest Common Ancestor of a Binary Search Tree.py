"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

	def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
		Node = root
		while Node:
			if Node.val > p.val & Node.val > q.val:
				Node = Node.left
			elif Node.val < p.val & Node.val < q.val:
				Node = Node.right
			else:
				return Node
#Compare the current node with p and q to see if they are on the same side. Once they are on different sides, the current node is the LCA.
