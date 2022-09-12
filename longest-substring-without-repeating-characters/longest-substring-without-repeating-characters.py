class Solution:
    # Runtime Complexity: O(n) to go over every character in the string
    # Space Complexity: O(n), since the set can grow to the size of the string
    # Total Time: 6 m
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSubstring, left = 0, 0
        chars = set()
        for right in range(len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[right])
            longestSubstring = max(longestSubstring, len(chars))
        return longestSubstring