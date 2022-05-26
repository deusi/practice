# Time Complexity: O(n) where n is the length of the input
# Space Complexity: O(1), since we use one variable to store the result
class Solution:
    def hammingWeight(self, n: int) -> int:
        ones = 0
        while n:
            ones += (n & 1)
            n = n >> 1
        return ones