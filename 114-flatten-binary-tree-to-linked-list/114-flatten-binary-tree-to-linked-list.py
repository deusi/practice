# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Runtime Complexity: O(n)
    # Space Complexity: O(n) due to recursion stack
    # Total Time: 17 m +30m for recursive approach
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        def convert(node):
            if not node:
                return node
            if not node.left and not node.right:
                return node
            left = convert(node.left)
            right = convert(node.right)
            if left:
                tmp = node.right
                node.right = node.left
                left.right = tmp
            node.left = None
            return right if right else left
        
        convert(root)
