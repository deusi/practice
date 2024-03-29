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
    # Runtime Complexity: O(n)
    # Space Complexity: O(n) to maintain the queue
    # Total Time: 8 m
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        queue = collections.deque([root])
        while queue:
            level = len(queue)
            prev = None
            for i in range(level -1, -1, -1):
                queue[i].next = prev
                prev = queue[i]
            for _ in range(level):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root