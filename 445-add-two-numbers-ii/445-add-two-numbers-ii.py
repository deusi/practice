# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num = 0
        l1Len, l2Len = 0, 0
        ptr1, ptr2 = l1, l2
        while ptr1:
            l1Len += 1
            ptr1 = ptr1.next
        while ptr2:
            l2Len += 1
            ptr2 = ptr2.next
        ptr1, ptr2 = l1, l2
        while l1Len > 0 and l2Len > 0:
            num *= 10
            if l1Len >= l2Len:
                num += ptr1.val
                ptr1 = ptr1.next
                l1Len -= 1
            if l2Len > l1Len:
                num += ptr2.val
                ptr2 = ptr2.next
                l2Len -= 1
        if num == 0:
            return ListNode(0)
        prev = None
        while num:
            cur = ListNode(num % 10)
            cur.next = prev
            prev = cur
            num = num // 10
        return prev
            
            
            
            
            