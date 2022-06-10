class Solution:
    # Runtime Complexity: O(n), since we go through each character once and add/remove operation is O(1)
    # Space Complexity: O(n), since we can store entire string if it has unique characters
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters = set()
        maxSubstring = 0
        left = 0
        for right in range(len(s)):
            if s[right] in characters:
                while s[right] in characters:
                        characters.remove(s[left])
                        left += 1
            characters.add(s[right])
            maxSubstring = max(maxSubstring, right - left + 1)
        return maxSubstring