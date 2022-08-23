# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        length = 0
        ptr = head
        # find the length of the ll
        while ptr:
            length += 1
            ptr = ptr.next
        mid = (length // 2 + length % 2) - 1
        midNode = head
        
        # get the middle node of the ll
        for _ in range(mid):
            midNode = midNode.next
        cur, prev = midNode.next, None
        midNode.next = None
        
        # reverse the second half of the ll
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
        return True