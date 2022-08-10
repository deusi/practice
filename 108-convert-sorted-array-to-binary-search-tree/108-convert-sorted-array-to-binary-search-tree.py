# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Runtime Complexity: O(n) to traverse every element in the array
    # Space Complexity: O(n) to construct the BST + recursion stack
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def bst(left, right):
            if left > right:
                return None
            mid = left + (right - left) // 2 
            node = TreeNode(nums[mid], bst(left, mid - 1), bst(mid + 1, right))
            return node
        return bst(0, len(nums) - 1)