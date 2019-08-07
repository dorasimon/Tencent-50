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