class Solution:
    # Runtime Complexity: O(n), since we add and pop the same elements
    # Space Complexity: O(n) to keep the stack
    # Total Time: 30 m
    def trap(self, height: List[int]) -> int:
        stack = []
        water, left, prev = 0, 0, 0
        for h in height:
            if h >= left:
                while stack:
                    water += left - stack.pop()
                left = h
            stack.append(h)
        while stack:
            e = stack.pop()
            prev = max(prev, e)
            water += prev - e
        return water