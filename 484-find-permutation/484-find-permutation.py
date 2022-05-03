class Solution:
    def findPermutation(self, s: str) -> List[int]:
        num, i = 1, 1
        perm = []
        for c in s:
            # if encountered 'I', push nums and decrease nums
            # That way we account for previous 'D'
            # and push only one num if no 'D' were encountered before
            if c == 'I':
                tmp = num + 1
                while num >= i:
                    perm.append(num)
                    num -= 1
                i, num = tmp, tmp
            else:
                num += 1
        # push any remaining nums to perm
        while num >= i:
            perm.append(num)
            num -= 1
        return perm