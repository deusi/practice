class Solution:
    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    def removePalindromeSub(self, s: str) -> int:
        if len(s) == 0:
            return 0
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return 2
            left += 1
            right -= 1
        return 1