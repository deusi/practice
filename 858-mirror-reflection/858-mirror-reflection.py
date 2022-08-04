class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        isEast = True
        curPos = q % p
        num = q // p
        while curPos > 0:
            isEast = not isEast
            num += (curPos + q) // p
            curPos = (curPos + q) % p
        if isEast and num % 2 == 0:
            return 0
        elif isEast:
            return 1
        return 2