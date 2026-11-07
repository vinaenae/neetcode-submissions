# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        queue = deque([root])
        if not root:
            return []
        while queue:
            temp = []
            for _ in range(len(queue)):
                num = queue.popleft()
                if num.left:
                    queue.append(num.left)
                if num.right:
                    queue.append(num.right)
                temp.append(num.val)
            output.append(temp)
        return output    









            

        
        