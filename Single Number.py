"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

	def singleNumber(self, nums: List[int]) -> int:
		while nums[0] in nums[1:]:
			nums = list(filter(lambda x: x != nums[0], nums))
		return nums[0]