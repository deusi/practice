"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def populate(node):
            if not node:
                return
            nextNode = None
            curNode = node
            prev = None
            while curNode:
                if not prev:
                    if curNode.left:
                        prev = curNode.left
                    elif curNode.right:
                        prev = curNode.right
                    nextNode = prev
                if prev:
                    if curNode.left and curNode.left != prev:
                        prev.next = curNode.left
                        prev = curNode.left
                    if curNode.right and curNode.right != prev:
                        prev.next = curNode.right
                        prev = curNode.right
                curNode = curNode.next
                
            populate(nextNode)
                
        populate(root)
        return root