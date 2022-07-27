# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Runtime Complexity: O(log n)
    # Space Complexity: O(1)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        minV, maxV = min(p.val, q.val), max(p.val, q.val)
        def lca(node):
            if node.val == minV or node.val == maxV or (node.val > minV and node.val < maxV):
                return node
            if node.val > minV:
                return lca(node.left)
            return lca(node.right)
        return lca(root)