class Solution:
    def countVowelStrings(self, n: int) -> int:
        count = 0
        vowels = ["a","e","i","o","u"]
        def rec(start, curLen):
            nonlocal count
            if start >= len(vowels) or curLen > n:
                return
            elif curLen == n:
                count += 1
                return
            else:
                for i in range(start, len(vowels)):
                    rec(i, curLen + 1)
        rec(0,0)
        return count