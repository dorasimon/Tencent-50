"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/contains-duplicate
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution1:

	def containsDuplicate(self, nums: List[int]) -> bool:
		return len(nums) != len(set(nums))


class Solution2:

	def containsDuplicate(self, nums: List[int]) -> bool:
		l = []
		for num in nums:
			if num not in l:
				l.append(num)
			else:
				return True
		return False 