class Solution:
    # Runtime Complexity: O(n), since we go over every element
    # Space Complexity: O(n), since stack can grow to the size of n
    # Total Time 15 m + 7 m to make it look prettier
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
            