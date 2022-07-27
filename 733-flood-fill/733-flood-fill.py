class Solution:
    # Runtime Complexity: O(m*n), we would have to go through every node if all of them are the same
    # Space Complexity: O(m*n), worst case is when the entire image is in old color
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        oldColor = image[sr][sc]
        image[sr][sc] = color
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        queue = collections.deque([[sr, sc]])
        while queue:
            r, c = queue.popleft()
            for d1, d2 in directions:
                if r+d1 >= m or c+d2 >= n or r+d1 < 0 or c+d2 < 0 or image[r+d1][c+d2] == color:
                    continue
                if image[r+d1][c+d2] == oldColor:
                    image[r+d1][c+d2] = color
                    queue.append([r+d1, c+d2])
        return image