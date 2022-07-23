class Solution:
    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    def longestPalindrome(self, s: str) -> int:
        longest, extra = 0, 0
        counter = collections.Counter(s)
        for value in counter.values():
            extra = max(extra, value % 2)
            longest += value - (value % 2)
        return longest + extra