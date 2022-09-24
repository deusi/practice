# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l1
        rem = 0
        prev = None
        while l1 and l2:
            num = l1.val + l2.val + rem
            l1.val = num % 10
            rem = num // 10
            prev = l1
            l1, l2 = l1.next, l2.next
        while l1:
            num = l1.val + rem
            l1.val = num % 10
            rem = num // 10
            prev = l1
            l1 = l1.next
        while l2:
            num = l2.val + rem
            prev.next = ListNode(num % 10)
            rem = num // 10
            prev = prev.next
            l2 = l2.next
        if rem:
            prev.next = ListNode(rem)
        return head