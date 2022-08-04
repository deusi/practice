class Solution:
    # Runtime Complexity: O(b), where b is the number of bounces to reach a deflector
    # Space Complexity: O(1)
    def mirrorReflection(self, p: int, q: int) -> int:
        isEast = True
        num, curPos = q // p, q % p
        while curPos > 0:
            isEast = not isEast
            num += (curPos + q) // p
            curPos = (curPos + q) % p
        if isEast:
            return 0 if num % 2 == 0 else 1
        return 2