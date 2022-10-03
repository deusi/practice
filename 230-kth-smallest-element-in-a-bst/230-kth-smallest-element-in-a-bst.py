# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Runtime Complexity: O(n), since the node is the rightmost leaf in the worst case
    # Space Complexity: O(n) due to stack recursion
    # Total Time: 20m (for rec sol)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        def findElem(node):
            nonlocal count
            if not node:
                return 0
            ans = 0
            if node.left and count < k:
                ans += findElem(node.left)
            count += 1
            if count == k:
                return node.val
            if node.right and count < k:
                ans += findElem(node.right)
            return ans
        return findElem(root)