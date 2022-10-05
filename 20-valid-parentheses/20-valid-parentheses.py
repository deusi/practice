class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p == '(' or p == '[' or p == '{':
                stack.append(p)
            else:
                if not stack:
                    stack.append(p)
                    break
                l = stack[-1]
                if l == '(' and p != ')' or l == '[' and p != ']' or l == '{' and p != '}':
                    break
                stack.pop()
        return len(stack) == 0
            