class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = [10**5 + 1 for _ in range(26)]
        for i, char in enumerate(s):
            iOrd = ord(char) - ord('a')
            if chars[iOrd] != 10**5 + 1:
                chars[iOrd] = 10**5 + 2
            else:
                chars[iOrd] = i
        
        minIdx = min(chars)
        return -1 if minIdx > 10**5 else minIdx