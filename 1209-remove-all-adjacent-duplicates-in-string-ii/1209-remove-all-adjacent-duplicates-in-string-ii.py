class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [(-1, -1)]
        for c in s:
            if stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])
            if stack[-1][1] == k:
                stack.pop()
        return "".join(char * count for char, count in stack[1:])