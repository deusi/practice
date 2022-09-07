# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Runtime Complexity: O(n), since we nee to visit every node and then turn the result into string
    # Space Complexity: O(n) to store the string
    def tree2str(self, root: Optional[TreeNode]) -> str:
        string = []
        def dfs(node, string):
            if not node:
                return
            string.append(str(node.val))
            string.append("(")
            dfs(node.left, string)
            string.append(")") if (node.right and not node.left) or node.left else string.pop()
            string.append("(")
            dfs(node.right, string)
            string.pop() if string[-1] == "(" else string.append(")")
        dfs(root, string)
        return "".join(string)