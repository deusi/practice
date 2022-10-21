class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        maxDepth = 0
        for c in s:
            if c == '(':
                stack.append(c)
                maxDepth = max(maxDepth, len(stack))
            elif c == ')':
                stack.pop()
        return maxDepth