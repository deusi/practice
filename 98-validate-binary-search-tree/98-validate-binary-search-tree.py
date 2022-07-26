# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Runtime Complexity O(n)
    # Space Complexity: O(n)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, -math.inf, math.inf)]
        while stack:
            node, minVal, maxVal = stack.pop()
            if node.val >= maxVal or node.val <= minVal:
                return False
            if node.right:
                stack.append((node.right, node.val, maxVal))
            if node.left:
                stack.append((node.left, minVal, node.val))
        return True