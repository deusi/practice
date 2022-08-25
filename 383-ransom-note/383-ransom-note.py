class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        randDict = collections.Counter(magazine)
        for letter in ransomNote:
            if letter not in randDict or randDict[letter] <= 0:
                return False
            randDict[letter] -= 1
        return True