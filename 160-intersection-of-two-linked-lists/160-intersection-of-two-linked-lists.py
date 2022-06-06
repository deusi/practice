# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA, lenB = 0, 0
        nodeA, nodeB = headA, headB
        while nodeA:
            lenA += 1
            nodeA = nodeA.next
        while nodeB:
            lenB += 1
            nodeB = nodeB.next
        nodeA, nodeB = headA, headB
        while lenA > lenB:
            nodeA = nodeA.next
            lenA -= 1
        while lenB > lenA:
            nodeB = nodeB.next
            lenB -= 1
        while lenA > 0:
            if nodeA is nodeB:
                return nodeA
            nodeA = nodeA.next
            nodeB = nodeB.next
            lenA -= 1
        return None