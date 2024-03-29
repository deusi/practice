# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Total Time: 12m
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result
        queue = collections.deque([root])
        while queue:
            result.append(queue[-1].val)
            level = len(queue)
            for _ in range(level):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result