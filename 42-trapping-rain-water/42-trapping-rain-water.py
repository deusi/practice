class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        water = 0
        left = 0
        for h in height:
            if h >= left:
                minWall = min(left, h)
                while stack:
                    water += minWall - stack.pop()
                left = h
            stack.append(h)
            prev = 0
        while stack:
            e = stack.pop()
            prev = max(prev, e)
            minWall = min(left, prev)
            water += minWall - e
        return water