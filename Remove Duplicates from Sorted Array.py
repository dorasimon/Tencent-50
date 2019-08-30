"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		pointer1 = 0
		pointer2 = 1
		while pointer2 < len(nums):
		#Make sure that pointer2 doesn't go outside the array.
			if nums[pointer2] == nums[pointer1]:
				del nums[pointer2]
				#When the two elements are equal, delete the second one. Keep deleting the second one until the two elements are not equal.
			else:
				pointer1 += 1
				pointer2 += 1
				#When they are not equal, move both pointers.
		return nums
		