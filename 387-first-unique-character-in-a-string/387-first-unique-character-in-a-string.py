class Solution:
    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    def firstUniqChar(self, s: str) -> int:
        chars = collections.Counter(s)
        for idx, c in enumerate(s):
            if chars[c] == 1:
                return idx
        return -1
        