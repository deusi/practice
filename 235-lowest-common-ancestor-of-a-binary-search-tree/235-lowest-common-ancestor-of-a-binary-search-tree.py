# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(node):
            if node.val == p.val or node.val == q.val or (node.val > min(p.val, q.val) and node.val < max(p.val, q.val)):
                return node
            if node.val > p.val:
                return lca(node.left)
            return lca(node.right)
        return lca(root)