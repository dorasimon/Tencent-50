"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

	def isValid(self, s: str):
		if len(s) % 2 != 0:
			return False 
		#If s has an odd number of elements, it must be false.
		else:
			pairs = ["()", "[]", "{}"]
			while any(x in s for x in pairs):
				for pair in pairs:
					s = s.replace(pair, "")
		#Remove every paired bracket from s and see if there's anything left.
			return s == ""