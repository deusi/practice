class Solution:
    # Runtime Complexity: O(2^n) - no, much harder
    # Space Complexity: O(2^n) - no, much harder
    # Total Time: 20m
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def generatePar(o, c, curPar):
            if len(curPar) == 2 * n:
                result.append("".join(curPar))
                return
            if o > 0:
                curPar.append('(')
                generatePar(o - 1, c, curPar)
                curPar.pop()
            if c > o:
                curPar.append(')')
                generatePar(o,  c - 1, curPar)
                curPar.pop()
            return
        generatePar(n, n, [])
        return result