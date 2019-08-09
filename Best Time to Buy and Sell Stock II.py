"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

	def maxProfit(self, prices: List[int]) -> int:
		profit = 0
		for i in range(0, len(prices) - 1):
			if prices[i + 1] > prices[i]:
				profit += prices[i + 1] - prices[i]
				#Traverse the list. When the next element is greater than one element, calculate the difference and add it to the profit.
		return profit