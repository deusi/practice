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
    # O(n), since we go over each node once
    # O(1), no extra space
    # Total Time: 50m for follow-up solution
    def connect(self, root: 'Node') -> 'Node':
        curNode = root
        while curNode:
            nextNode = None
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
                
            curNode = nextNode       
        
        return root