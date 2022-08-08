# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        while root.left or root.right:
            queue = collections.deque([root])
            leaves = []
            while queue:
                node = queue.popleft()
                leftnode = node.left
                rightnode = node.right
                if leftnode:
                    if not leftnode.left and not leftnode.right:
                        leaves.append(leftnode.val)
                        node.left = None
                    else:
                        queue.append(leftnode)
                if rightnode:
                    if not rightnode.left and not rightnode.right:
                        leaves.append(rightnode.val)
                        node.right = None
                    else:
                        queue.append(rightnode)
            output.append(leaves)
        output.append([root.val])
        return output
                