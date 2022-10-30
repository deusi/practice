class Solution:
    # Runtime Complexity: O(n) to build stack, invalid and string
    # Space Complexity: O(n) to store stack
    # Total Time: 14 m
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] not in '()':
                continue
            elif stack and stack[-1][0] == '(' and s[i] == ')':
                stack.pop()
            else:
                stack.append((s[i], i))
        invalid = set()
        for c, i in stack:
            invalid.add(i)
        string = []
        for i in range(len(s)):
            if i in invalid:
                continue
            string.append(s[i])
        return ''.join(string)