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
        pV, qV = p.val, q.val
        def lca(node):
            if node.val == pV or node.val == qV or (node.val > min(pV, qV) and node.val < max(pV, qV)):
                return node
            if node.val > p.val:
                return lca(node.left)
            return lca(node.right)
        return lca(root)