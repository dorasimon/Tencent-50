"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution1:

	def singleNumber(self, nums: List[int]) -> int:
		while nums[0] in nums[1:]:
			nums = list(filter(lambda x: x != nums[0], nums))
			#Compare the first element with the rest of the list. If there is another one, remove them from the list and start over again.
		return nums[0]


class Solution2:

	def singleNumber(self, nums: List[int]) -> int:
		i = 0
		for num in nums:
			i ^= num
		return i