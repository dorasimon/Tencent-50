"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from itertools import combinations

class Solution:

	def subsets(self, nums: List[int]) -> List[List[int]]:
		subsets = []
		length = len(nums)
		while length >= 0:
			subset = combinations(nums, length)
			for i in subset:
				subsets.append(list(i))
			length -= 1
			#Return all combinations based on size from the length of nums to 0.
		return subsets