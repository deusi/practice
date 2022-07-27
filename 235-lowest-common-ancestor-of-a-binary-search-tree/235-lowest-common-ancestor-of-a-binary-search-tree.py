# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Runtime Complexity: O(log n) (degenerates to O(n) for unbalanced tree) 
    # Space Complexity: O(n), due to recursion stack
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        minV, maxV = min(p.val, q.val), max(p.val, q.val)
        node = root
        while node:
            if node.val == minV or node.val == maxV or (node.val > minV and node.val < maxV):
                return node
            elif node.val > minV:
                node = node.left
            else:
                node = node.right