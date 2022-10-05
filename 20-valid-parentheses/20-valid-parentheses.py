class Solution:
    #
    #
    # Total Time 15 m + 
    def isValid(self, s: str) -> bool:
        stack = []
        pMap = {'(': ')', '[': ']', '{': '}'}
        for p in s:
            if p in pMap:
                stack.append(p)
            elif not stack or p != pMap[stack[-1]]:
                return False
            else:
                stack.pop()
        return len(stack) == 0
            