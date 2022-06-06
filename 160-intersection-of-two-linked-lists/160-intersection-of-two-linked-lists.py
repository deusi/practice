# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Time Complexity: O(m + n), since we visit every element of the lists once
    # Space Complexity O(m + n), since in the worst case we store each element in the set
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited = set()
        nodeA, nodeB = headA, headB
        while nodeA or nodeB:
            if nodeA:
                if nodeA in visited:
                    return nodeA
                visited.add(nodeA)
                nodeA = nodeA.next
            if nodeB:
                if nodeB in visited:
                    return nodeB
                visited.add(nodeB)
                nodeB = nodeB.next
                
        return None