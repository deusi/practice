# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        queue = deque([[original, cloned]])
        while queue:
            orig, clon = queue.popleft()
            if orig == target:
                return clon
            if orig.left:
                queue.append([orig.left, clon.left])
            if orig.right:
                queue.append([orig.right, clon.right])
        return None
        