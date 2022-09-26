# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1, stack2 = [], []
        while l1 or l2:
            if l1:
                stack1.append(l1.val)
                l1 = l1.next
            if l2:
                stack2.append(l2.val)
                l2 = l2.next
        prev = None
        rem = 0
        while rem or stack1 or stack2:
            num1, num2 = 0, 0
            if stack1:
                num1 = stack1.pop()
            if stack2:
                num2 = stack2.pop()
            num = num1 + num2 + rem
            rem = num // 10
            cur = ListNode(num % 10, prev)
            prev = cur
            
        return prev