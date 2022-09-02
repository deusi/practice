# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        queue = collections.deque([root])
        while queue:
            levelLen = len(queue)
            avg = 0
            for _ in range(levelLen):
                node = queue.popleft()
                avg += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(avg / levelLen)
        return result