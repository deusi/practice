# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Runtime Complexity: O(m + n) - m, n - length of lls
    # Space Complexity: O(1) - moving pointers
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode(-101, None)
        node = root
        while list1 and list2:
            if list2.val < list1.val:
                node.next = list2
                list2 = list2.next
            else:
                node.next = list1
                list1 = list1.next
            node = node.next 
        node.next = list1 or list2
        return root.next