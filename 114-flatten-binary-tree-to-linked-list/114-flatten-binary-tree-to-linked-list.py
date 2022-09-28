# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Runtime Complexity: O(n) to go over every node to add it to inorder list and n to traverse the list and set up the pointers
    # Space Complexity: O(n) to keep the list of nodes
    # Total Time: 17 m
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        stack = [root]
        inorder = []
        while stack:
            node = stack.pop()
            inorder.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                node.left = None
        for i in range(1, len(inorder)):
            inorder[i-1].right = inorder[i]