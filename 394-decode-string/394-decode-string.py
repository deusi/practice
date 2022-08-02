class Solution:
    def decodeString(self, s: str) -> str:
        def bt(i):
            st = ""
            while i < len(s):
                n = 0
                if s[i] == ']':
                    return i, st
                elif s[i].isdigit():
                    while s[i].isdigit():
                        n *= 10
                        n += int(s[i])
                        i += 1
                    i, t = bt(i + 1)
                    st += n * t
                else:
                    st += s[i]
                i += 1
            return i, st
            
        idx = 0
        decoded = ""
        while idx < len(s):
            num = 0
            if s[idx].isdigit():
                while s[idx].isdigit():
                    num *= 10
                    num += int(s[idx])
                    idx += 1
                idx, temp = bt(idx + 1)
                print(num, temp)
                decoded += num * temp
            else:
                decoded += s[idx]
            idx += 1
        return decoded