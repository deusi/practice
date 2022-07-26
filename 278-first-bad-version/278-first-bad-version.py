# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    # Runtime Complexity: O(log n)
    # Space Complexity: O(1)
    def firstBadVersion(self, n: int) -> int:
        low, high = 1, n
        while low <= high:
            mid = low + (high - low) // 2
            curBad = isBadVersion(mid)
            if curBad and (mid == 1 or not isBadVersion(mid - 1)):
                return mid
            elif curBad:
                high = mid - 1
            else:
                low = mid + 1