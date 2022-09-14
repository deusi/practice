# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.pp = 0
        def dfs(node, path, elementCount):
            path[node.val] = path.get(node.val, 0) + 1
            elementCount += 1
            if not node.left and not node.right:
                checkPalidrome(path, elementCount)
            if node.left:
                dfs(node.left, path, elementCount)
            if node.right:
                dfs(node.right, path, elementCount)
            path[node.val] -= 1
            if path[node.val] == 0:
                del path[node.val]
            elementCount -= 1
            
        def checkPalidrome(counter, n):
            oneOdd = n % 2 == 1
            for v in counter.values():
                if oneOdd and v % 2 == 1:
                    oneOdd = False
                    continue
                if v % 2 == 0:
                    continue
                return False
            self.pp += 1
            return True
        
        dfs(root, collections.Counter(), 0)
        return self.pp