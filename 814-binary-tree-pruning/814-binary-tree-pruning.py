# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Runtime Complexity: O(n) to visit every node
    # Space Complexity: O(n), due to stack recursion
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # handle special case of completely prunned tree
        sentinel = TreeNode(0, None, root)
        def dfs(node):
            if not node:
                return False
            left, right = dfs(node.left), dfs(node.right)
            if not left:
                node.left = None
            if not right:
                node.right = None
            return left or right or node.val == 1
        dfs(sentinel)
        return sentinel.right