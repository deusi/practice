# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        string = []
        def dfs(node, string):
            if not node:
                return
            string.append(str(node.val))
            string.append("(")
            dfs(node.left, string)
            if (node.right and not node.left) or node.left:
                string.append(")")
            else:
                string.pop()
            string.append("(")
            dfs(node.right, string)
            if string[-1] == "(":
                string.pop()
            else:
                string.append(")")
        dfs(root, string)
        return "".join(string)