class Solution:
    def longestValidParentheses(self, s: str) -> int:
        longest = 0
        stack = [-1]
        for i, p in enumerate(s):
            if p == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack):
                    longest = max(longest, i - stack[-1])
                else:
                    stack.append(i)
        return longest