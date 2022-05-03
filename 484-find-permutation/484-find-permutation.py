class Solution:
    def findPermutation(self, s: str) -> List[int]:
        num, i = 1, 1
        perm = []
        for c in s:
            if c == 'I':
                tmp = num + 1
                while num >= i:
                    perm.append(num)
                    num -= 1
                i, num = tmp, tmp
            else:
                num += 1
        while num >= i:
            perm.append(num)
            num -= 1
        return perm