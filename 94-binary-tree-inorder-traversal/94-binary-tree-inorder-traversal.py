# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Runtime: O(n)
    # Space: O(n)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal = []
        if not root:
            return traversal
        def inorder(node):
            if node.left:
                inorder(node.left)
            traversal.append(node.val)
            if node.right:
                inorder(node.right)
        inorder(root)
        return traversal