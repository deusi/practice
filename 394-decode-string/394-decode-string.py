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
                elif s[i] == ']':
                    return i, "".join(strList)
                elif s[i].isdigit():
                    numList.append(s[i])
                else:
                    strList.append(s[i])
                i += 1 
            return "".join(strList)
        return decode(0)