class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowelCount = [1, 1, 1, 1, 1]
        if n == 1:
            return sum(vowelCount)
        while n > 1:
            for i in range(1, len(vowelCount)):
                vowelCount[i] += vowelCount[i - 1]
            n -= 1
        return sum(vowelCount)