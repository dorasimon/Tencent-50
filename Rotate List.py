"""
Given a linked list, rotate the list to the right by k places, where k is non-negative.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

	def rotateRight(self, head: ListNode, k: int) -> ListNode:
		tmp = []
		iHead = head
		while head:
			tmp.append(head.val)
			head = head.next
		length = len(tmp)
		if length == 0 or k == 0:
			return iHead
		else:
			tmp = tmp[length - k % length:] + [:length - k % length]
		newHead = node = ListNode(None)
		for i in range(length):
			node.next = ListNode(tmp[i])
			node = node.next
		return newHead.next