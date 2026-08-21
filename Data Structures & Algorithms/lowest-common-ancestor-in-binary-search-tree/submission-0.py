# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return
        minimum = p.val if p.val < q.val else q.val
        maximum = p.val if p.val > q.val else q.val

        if root.val >= minimum and root.val <= maximum:
            return root

        if root.val > maximum:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < minimum:
            return self.lowestCommonAncestor(root.right, p, q)
        