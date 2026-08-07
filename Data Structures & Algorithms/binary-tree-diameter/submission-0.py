# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:    
        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            return 1 + max(left, right)

        if not root:
            return 0

        left = dfs(root.left)
        right = dfs(root.right)
        di = left + right

        return max(self.diameterOfBinaryTree(root.left),
         self.diameterOfBinaryTree(root.right), 
         di)
        