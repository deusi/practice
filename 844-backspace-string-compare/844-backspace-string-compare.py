class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def nextValidChar(str, idx):
            backspaces = 0
            while idx >= 0:
                if str[idx] == '#':
                    backspaces += 1
                elif backspaces == 0:
                    break
                else:
                    backspaces -= 1
                idx -= 1
            return idx
        
        idxS, idxT = len(s) - 1, len(t) - 1
        while idxS > -1 or idxT > -1:
            nextS, nextT = nextValidChar(s, idxS), nextValidChar(t, idxT)
            if nextS < 0 and nextT < 0:
                return True
            elif nextS < 0 or nextT < 0 or s[nextS] != t[nextT]:
                return False
            idxS, idxT = nextS - 1, nextT - 1
        return True