class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p): return []
        pLetters = collections.Counter(p)
        pUniqueLetters = len(pLetters)
        anagrams = []
        left = 0
        for right in range(len(s)):
            if s[right] in pLetters:
                if pLetters[s[right]] - 1 == 0:
                    pUniqueLetters -= 1
                pLetters[s[right]] -= 1
            if pUniqueLetters == 0:
                anagrams.append(left)
            if right >= len(p) - 1:
                if s[left] in pLetters:
                    if pLetters[s[left]] == 0:
                        pUniqueLetters += 1
                    pLetters[s[left]] += 1
                left += 1
        return anagrams