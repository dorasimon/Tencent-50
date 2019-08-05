class Solution:

	def isValid(self, s: str):
		if len(s) % 2 != 0:
			return False #If s has an odd number of elements, it must be false.#
		else:
			pairs = ["()", "[]", "{}"]
			while any(x in s for x in pairs):
				for pair in pairs:
					s = s.replace(pair, "")
			return s == ""