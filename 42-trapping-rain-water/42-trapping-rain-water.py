class Solution:
    # Runtime Complexity: 
    # Space Complexity: 
    # Total Time: 30 m
    def trap(self, height: List[int]) -> int:
        stack = []
        water, left, prev = 0, 0, 0
        for h in height:
            if h >= left:
                minWall = min(left, h)
                while stack:
                    water += minWall - stack.pop()
                left = h
            stack.append(h)
        while stack:
            e = stack.pop()
            prev = max(prev, e)
            minWall = min(left, prev)
            water += minWall - e
        return water