"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

	def maxProfit(self, prices: List[int]) -> int:
		minPrice = float('inf')
		maxProfit = 0
		for i in range(len(prices)):
			minPrice = min(minPrice, prices[i])
			maxProfit = max(maxProfit, prices[i] - minPrice)
		return maxProfit