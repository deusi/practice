# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Runtime Complexity O(n log n) - n to go over every element of bt and O(1) to iterate over counter to check if palindrome, but it's done only at leaf level h = log n
    # Space Complexity: O(1), since array is fixed
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.pp = 0
        path = [0 for _ in range(9)]
        
        def dfs(node, path):
            path[node.val - 1] += 1
            if not node.left and not node.right:
                checkPalidrome(path)
            if node.left:
                dfs(node.left, path)
            if node.right:
                dfs(node.right, path)
            path[node.val - 1] -= 1
            
        def checkPalidrome(counter):
            n = len(counter)
            oneOdd = n % 2 == 1
            for v in counter:
                if oneOdd and v % 2 == 1:
                    oneOdd = False
                    continue
                if v % 2 == 0:
                    continue
                return False
            self.pp += 1
            return True
        
        dfs(root, path)
        return self.pp