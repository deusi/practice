"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    # Runtime Complexity: O(n)
    # Space Complexity: O(n), due to recursion stack
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        def preorder_rec(node):
            if not node:
                return
            result.append(node.val)
            for c in node.children:
                preorder_rec(c)
        preorder_rec(root)
        return result
        