class Solution:
    def decodeString(self, s: str) -> str:
        def decode(i):
            strList, numList = [], []
            while i < len(s):
                if s[i] == '[':
                    i, retStr = decode(i + 1)
                    num = int("".join(numList))
                    numList = []
                    strList.append(num * retStr)
                if i < len(s) and s[i] == ']':
                    return i + 1, "".join(strList)
                if i < len(s) and s[i].isdigit():
                    numList.append(s[i])
                else:
                    if i < len(s):
                        strList.append(s[i])
                i += 1 
            return "".join(strList)
        return decode(0)