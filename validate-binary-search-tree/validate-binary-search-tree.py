# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Runtime Complexity: O(n)
    # Space Complexity: O(n) due to stack recursion
    # Total Time: 42 m for recursive and (failed) solutions
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        minVal = -inf
        def inorder(node):
            nonlocal minVal
            if not node:
                return True
            left = inorder(node.left)
            if node.val <= minVal:
                return False
            minVal = node.val
            right = inorder(node.right)
            return left and right
        return inorder(root)