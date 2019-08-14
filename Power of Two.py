class Solution1:

	def isPowerOfTwo(self, n: int) -> bool:
		if n == 1:
			return True
		else:
			while int(str(n)[-1]) % 2 == 0:
				n = n / 2
				if n == 1:
					return True
					break
					#Check the last digit of n. If it's odd, return false; if it's even, divide n by 2 until it becomes odd or 1.
		return False


class Solution2:

	def isPowerOfTwo(self, n: int) -> bool:
		return n > 0 and n & (n - 1) == 0