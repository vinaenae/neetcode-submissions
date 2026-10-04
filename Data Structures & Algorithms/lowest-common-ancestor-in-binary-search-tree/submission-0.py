# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        temp = root
        if p == root or q == root:
            return root
        if (p.val < root.val and q.val > root.val) or (q.val < root.val and p.val > root.val):
            return root
        if p.val < root.val and q.val < root.val:
            val = self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            val = self.lowestCommonAncestor(root.right, p, q)
        return val