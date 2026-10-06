# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, largest):
            if not root:
                return 0

            number_good = 0

            if root.val >= largest:
                number_good = 1

            largest = max(largest, root.val)
            number_good += dfs(root.left, largest)
            number_good += dfs(root.right, largest)

            return number_good
        
        return dfs(root, largest = root.val)

        