# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.number_good = 0
        def dfs(root, largest):
            if not root:
                return
            if root.val >= largest:
                self.number_good += 1        

            tmp = largest    
            largest = max(largest, root.val)
            dfs(root.left, largest)
            dfs(root.right, largest)
            
            largest = tmp
        
        dfs(root, largest = root.val)
        return self.number_good

        