class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        num = 1
        while num <= n:
            if num == n:
                return True
            num = num * 3
        return False