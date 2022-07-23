class Solution:
    def longestPalindrome(self, s: str) -> int:
        longest = 0
        extra = False
        counter = collections.Counter(s)
        for value in counter.values():
            if value % 2 == 0:
                longest += value
            elif value % 2 == 1:
                longest += value - 1
                extra = True
        if extra:
            longest += 1
        return longest