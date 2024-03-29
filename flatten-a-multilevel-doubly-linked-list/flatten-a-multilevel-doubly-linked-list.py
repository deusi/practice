"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    # Runtime Complexity: O(n), where n is the length of the flattened list
    # Space Complexity: O(k), where k is the depth of multilevel ll
    # Total Time: 22 m
    def flatten(self, head: 'Node') -> 'Node':
        def recFlatten(node):
            prev = None
            while node:
                if node.child:
                    flattened = recFlatten(node.child)
                    flattened.next = node.next
                    if node.next:
                        node.next.prev = flattened
                    node.next = node.child
                    node.child.prev = node
                    node.child = None
                    node = flattened
                prev = node
                node = node.next
            return prev
        recFlatten(head)
        return head
        