# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.number_good = 0
        self.largest = root.val
        def dfs(root):
            if not root:
                return
            if root.val >= self.largest:
                self.number_good += 1        

            tmp = self.largest    
            self.largest = max(self.largest, root.val)
            dfs(root.left)
            dfs(root.right)
            
            self.largest = tmp
        
        dfs(root)
        return self.number_good

        