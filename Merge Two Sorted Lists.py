class Solution:

	def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
		prehead = ListNode
		fixedhead = prehead
		while l1 and l2:
			if l1.val < l2.val:
				prehead.next = l1
				l1 = l1.next
			else:
				prehead.next = l2
				l2 = l2.next
			prehead = prehead.next
		if l1:
			prehead.next = l1
		else:
			prehead.next = l2
		return fixedhead.next