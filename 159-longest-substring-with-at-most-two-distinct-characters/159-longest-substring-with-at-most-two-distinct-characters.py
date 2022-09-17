class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        substrLength = 0
        left = 0
        counter = {}
        for right in range(len(s)):
            rWord = s[right]
            counter[rWord] = counter.get(rWord, 0) + 1
            while len(counter) > 2:
                lWord = s[left]
                counter[lWord] -= 1
                if counter[lWord] == 0:
                    del counter[lWord]
                left += 1
            substrLength = max(substrLength, right - left + 1)
        return substrLength