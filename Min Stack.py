"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/min-stack
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Minstack:

	def __init__(self):
		self.items = [] #The current stack#
		self.min_items = [] #The min stack#

	def push(self, x):
    	self.items.append(x) #Add element x on top of the current stack."
		if len(self.min_items) == 0 or x <= self.min_items[-1]:
			self.min_items.append(x) #Add x on top of the min stack as well when it's empty or when x is smaller than or equal to its last element.#

	def pop(self):
		if self.top() == self.getMin():
			self.min_items.pop()
		return self.items.pop() #Always remove the last element from the current stack. If it equals the last element on the min stack, remove it from the min stack as well.#

	def top(self):
    	return self.items[-1] #Return the last element on stack.#

	def getMin(self):
    	return self.min_items[-1] #Return the last element on the min stack.#