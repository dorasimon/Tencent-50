"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/container-with-most-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        leftIndex = 0
        while leftIndex < len(height) - 1:
            for rightIndex in range(leftIndex + 1, len(height)):
                area = min(height[leftIndex], height[rightIndex]) * (rightIndex - leftIndex)
                if area > maxArea:
                    maxArea = area
            leftIndex += 1
        return maxArea