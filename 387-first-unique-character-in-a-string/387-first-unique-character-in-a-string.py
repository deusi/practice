class Solution:
    # Runtime Complexity: O(n)
    # Space Complexity: O(1), since alphabet consists of 26 letters
    def firstUniqChar(self, s: str) -> int:
        chars = collections.Counter(s)
        for idx, c in enumerate(s):
            if chars[c] == 1:
                return idx
        return -1
        