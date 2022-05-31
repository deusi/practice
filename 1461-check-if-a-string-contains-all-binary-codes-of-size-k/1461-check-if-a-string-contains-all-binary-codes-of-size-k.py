class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        number = 1 << k
        contains = set()
        for i in range(0, len(s) - k + 1):
            if s[i:i+k] in contains:
                continue
            contains.add(s[i:i+k])
        print(contains)
        return number == len(contains)