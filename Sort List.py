"""
Sort a linked list in O(n log n) time using constant space complexity.
"""


class Solution:

	def sortList(self, head: ListNode) -> ListNode:
		if head == None or head.next == None:
			return head

		new_head = head
		node_list = []
		while head != None:
			node_list.append(head.val)
			head = head.next
		node_list.sort()

		head = new_head
		i = 0
		while head != None:
			head.val = node_list[i]
			head = head.next
			i += 1

		return new_head