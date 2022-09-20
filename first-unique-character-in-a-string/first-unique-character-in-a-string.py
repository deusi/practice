class Solution:
    # Runtime Complexity: O(n) to go over the string
    # Space Complexity: O(1), since there are at most 26 letters to consider
    # Total Time: 16 m - tried 3 different implementations
    def firstUniqChar(self, s: str) -> int:
        counter = collections.Counter(s)
        for i, char in enumerate(s):
            if counter[char] == 1:
                return i
        return -1
        