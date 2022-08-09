# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []
        cols = collections.defaultdict(list)
        queue = collections.deque([(root, 0)])
        while queue:
            node, lvl = queue.popleft()
            cols[lvl].append(node.val)
            if node.left:
                queue.append((node.left, lvl - 1))
            if node.right:
                queue.append((node.right, lvl + 1))
        minE, maxE = min(cols.keys()), max(cols.keys())
        output = []
        for i in range(minE, maxE + 1):
            output.append(cols[i])
        return output