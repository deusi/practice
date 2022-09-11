# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Runtime Complexity: O(n) to traverse each node
    # Space Complexity: O(n) for queue
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        queue = collections.deque([root])
        while queue:
            level = len(queue)
            for _ in range(level):
                node = queue.popleft()
                node.left, node.right = node.right, node.left
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)         
        return root