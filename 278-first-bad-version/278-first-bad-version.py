# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    # Runtime Complexity: O(log n)
    # Space Complexity: O(1)
    def firstBadVersion(self, n: int) -> int:
        low, high = 1, n
        while low < high:
            mid = low + (high - low) // 2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        return low