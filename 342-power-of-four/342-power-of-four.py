class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # 4^x = 2^2x
        mask = 1
        while mask < n:
            mask = mask << 2
        return mask == n