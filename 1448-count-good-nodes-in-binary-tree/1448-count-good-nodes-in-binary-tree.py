# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Runtime Complexity: O(n), since we need to go through entire tree
    # Space Complexity: O(n), if the is unbalanced and formes a ll
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        stack = [(root, root.val)]
        while stack:
            node, maxVal = stack.pop()
            if node.val >= maxVal:
                count += 1
                maxVal = node.val
            if node.left:
                stack.append((node.left, maxVal))
            if node.right:
                stack.append((node.right, maxVal))
        return count