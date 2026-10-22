# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        traverse = []
        if not root:
            return traverse
        queue = deque([root])
        while queue:
            internal = []
            for i in range(len(queue)):
                value = queue.popleft()
                internal.append(value.val)
                if value.left:
                    queue.append(value.left)
                if value.right:
                    queue.append(value.right)
            traverse.append(internal)
        return traverse        






            

        
        