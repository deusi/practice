# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Runtime Complexity: O(n log n) - n to traverse each level of leaf nodes , log n to go over tree height 
    # assuming tree is balanced, worst case could be degenerated to O(n^2)
    # Space Complexity: O(n) 
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        while root.left or root.right:
            queue = collections.deque([root])
            leafs = []
            while queue:
                node = queue.popleft()
                leftnode = node.left
                rightnode = node.right
                if leftnode:
                    if not leftnode.left and not leftnode.right:
                        leafs.append(leftnode.val)
                        node.left = None
                    else:
                        queue.append(leftnode)
                if rightnode:
                    if not rightnode.left and not rightnode.right:
                        leafs.append(rightnode.val)
                        node.right = None
                    else:
                        queue.append(rightnode)
            output.append(leafs)
        output.append([root.val])
        return output
                