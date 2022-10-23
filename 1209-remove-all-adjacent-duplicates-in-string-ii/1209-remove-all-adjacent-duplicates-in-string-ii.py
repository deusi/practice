class Solution:
    # Runtime Complexity: O(n) to go over every element of the string
    # Space Complexity: O(n) to maintain the stack
    # Total Time: 12 m
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [(-1, -1)]
        for c in s:
            if stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        return "".join(char * count for char, count in stack[1:])