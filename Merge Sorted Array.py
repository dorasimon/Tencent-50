"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

	def merge(self, nums1: List[int], m: int, nums2: List[int], n:int) -> None:
		p = m + n -1
		p1 = m - 1
		p2 = n - 1
		while p1 >= 0 and p2 >= 0:
			if nums2[p2] > nums1[p1]:
				nums1[p] = nums2[p2]
				p2 -= 1
			else:
				num1[p] = nums1[p1]
				p1 -= 1
			p -= 1
		nums1[:p2 + 1] = nums[:p2 + 1
		#If nums2 still has elements left, replace nums1's beginning with nums2's residual elements.