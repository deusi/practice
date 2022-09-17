class Solution:
    # Runtime Complexity: O(n) to go over string of len n
    # Space Complexity: O(1), since hashmap contains at most three values
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        substrLength, left = 0, 0
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