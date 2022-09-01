# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Runtime Complexity: O(n), n - total number of nodes
    # Space Complexity: O(n), when the tree is unbalanced
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        seqLen = 0
        stack = [(root, root.val, 1)]
        while stack:
            node, prevVal, curLen = stack.pop()
            if node.val == prevVal + 1:
                curLen += 1
            else:
                curLen = 1
            seqLen = max(seqLen, curLen)
            if node.left:
                stack.append((node.left, node.val, curLen))
            if node.right:
                stack.append((node.right, node.val, curLen))
        return seqLen