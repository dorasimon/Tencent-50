"""
Sort a linked list in O(n log n) time using constant space complexity.
"""


class Solution:

	def sortList(self, head: ListNode) -> ListNode:
		if head == None or head.next == None:
			return head
		#Check if the linked list is empty or only has one element.

		new_head = head
		node_list = []
		while head != None:
			node_list.append(head.val)
			head = head.next
		node_list.sort()
		#Transfer the linked list to a list and sort it.

		head = new_head
		i = 0
		while head != None:
			head.val = node_list[i]
			head = head.next
			i += 1

		return new_head
		#Transfer the list back to a linked list.