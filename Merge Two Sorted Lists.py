"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


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