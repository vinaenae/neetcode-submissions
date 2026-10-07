# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = {val: i for i, val in enumerate(inorder)}
        pre = 0

        def build(l, r):
            nonlocal pre
            if l > r:                      # empty range = no node
                return None

            root = TreeNode(preorder[pre]) # next root in preorder
            pre += 1                       # move to the next one

            mid = idx[root.val]            # where the root sits in inorder
            root.left = build(l, mid - 1)  # left side of the root
            root.right = build(mid + 1, r) # right side of the root
            return root

        return build(0, len(inorder) - 1)




        