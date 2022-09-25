"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    # Runtime Complexity: O(n), n to go over the list, create new nodes and and put them to a map and n to assign values to new list
    # Space Complexity: O(n), since map has to store all the mappings of origNodes -> newNodes
    # Total Time: 27 m
    def copyRandomList(self, head: 'Node') -> 'Node':
        sentinel = Node(-1)
        newList = sentinel
        ptr = head
        deep = {None: None}
        while ptr:
            newList.next = Node(ptr.val)
            newList = newList.next
            deep[ptr] = newList
            ptr = ptr.next
            
        newList = sentinel.next
        ptr = head
        while ptr:
            newList.random = deep[ptr.random]
            ptr = ptr.next
            newList = newList.next
            
        return sentinel.next
            