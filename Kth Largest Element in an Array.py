"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution1:

	def findKthLargest(self, nums: [int], k: int):
		nums = sorted(nums)
		return nums[-k]
		#Simply sort the list and get the Kth number from the end.#


import heapq

class Solution2:

	def findKthLargest(self, nums: [int], k: int):
		k_nums = []
		for num in nums[:k]:
			heapq.heappush(k_nums, num)
		#Create a list that always stores the largest K numbers. Heapq ensures that the smallest element gets pushed to the index position 0.#
		for num in nums[k:]:
			if num > k_nums[0]:
				heapq.heappush(k_nums, num)
				heapq.heappop(k_nums)
		#Add any number larger than the smallest number in the current largest K numbers to it and remove the first element.#
		return k_nums[0]