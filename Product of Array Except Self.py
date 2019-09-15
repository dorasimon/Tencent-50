"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/product-of-array-except-self
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


import numpy as np
class Solution:

	def productExceptSelf(self, nums: List[int]) -> List[int]:
		nums1 = list(nums)
		l = []
		for n in range(len(nums1)):
			del nums1[n]
			l.append(np.prod(nums1))
			nums1 = list(nums)
		return l