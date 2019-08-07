"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

	def mergeKLists(self, lists: List[ListNode]) -> ListNode:
		Sorted_List = []
		for i in lists:
			while i != None:
				Sorted_List.append(i.val)
				i = i.next
		Sorted_List.sort()
		#Merge the sorted lists into one list and sort it.
		Head_Node = ListNode(None)
		#Create the first node.
		Node = Head_Node
		#Copy the first node for moving the pointer.
		for j in Sorted_List:
			Node.next = ListNode(j)
			#Assign values to nodes.
			Node = Node.next
			#Link the nodes.
		return Head_Node.next
		#Return all the nodes except the first node.