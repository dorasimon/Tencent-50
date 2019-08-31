"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
	
	def maxSubArray(self, nums: List[int]) -> int:
		maxSubSum = nums[0]
		#Set the first element to be the default result.
		subSum = 0
		for num in nums:
			subSum += num
			#Calculate the new sum incrementally.
			if subSum > maxSubSum:
				maxSubSum = subSum
				#If the new sum is greater than the previous sum, update it.
			if subSum < 0:
				subSum = 0
				#Get rid of the negative elements before the first positive element.
		return maxSubSum