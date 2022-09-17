class Solution:
    # Runtime Complexity: O(n) to go over string of len n
    # Space Complexity: O(1), since hashmap contains at most three values
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        substrLength, left = 0, 0
        counter = {}
        for right in range(len(s)):
            rWord = s[right]
            counter[rWord] = right
            if len(counter) > 2:
                minVal = min(counter.values()) 
                del counter[s[minVal]]
                left = minVal + 1
            substrLength = max(substrLength, right - left + 1)
        return substrLength