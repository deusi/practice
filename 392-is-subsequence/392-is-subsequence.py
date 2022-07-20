class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        cur = 0
        for char in t:
            if s[cur] == char:
                cur += 1
                if cur == len(s):
                    return True
        return cur == len(s)