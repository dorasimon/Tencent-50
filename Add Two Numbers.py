"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

	def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
		l1_s = ""
		l2_s = ""
		while l1:
			l1_s += str(l1.val)
			l1 = l1.next
		l1_s = l1_s[::-1]
		while l2:
			l2_s += str(l2.val)
			l2 = l2.next
		l2_s = l2_s[::-1]
		#Turn both linked lists to strings, and reverse them.
		total_s = str(int(l1_s) + int(l2_s))
		#Turn both strings to integers, and add them up.
		tmp_node = ListNode(None)
		node = tmp_node
		for x in total_s[::-1]:
			if not tmp_node.val:
				tmp_node.val = x
			else:
				tmp_node.next = ListNode(x)
				tmp_node = tmp_node.next
		return node
		#Turn the sum to a linked list.