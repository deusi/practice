# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Runtime Complexity: O(n), n/2 for finding the middle point, n/2 for reversing the ll, n/2 to compare the ll
    # Space Complexity: O(1)
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur, fast = head, head
        while fast and fast.next:
            cur = cur.next
            fast = fast.next
            if fast:
                fast = fast.next
        
        # reverse the second half of the ll
        prev = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
            
        # compare 1st and 2nd halfs
        while prev and head:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        # TODO: restore the ll
        return True