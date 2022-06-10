class Solution:
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