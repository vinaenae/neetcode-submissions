from collections import deque
class Solution:
    def jump(self, nums: List[int]) -> int:
        def bfs(nums):
            min_jumps = 0
            if len(nums) == 1:
                return 0
            queue = deque([[nums[0], 0]])
            seen = set()
            while queue:
                for _ in range(len(queue)):
                    elem, index = queue.popleft()
                    if elem == 0:
                        continue
                    i = 1
                    while i <= elem:
                        t = index + i
                        if t >= len(nums) - 1:
                            min_jumps +=1
                            return min_jumps
                        if t not in seen:
                            queue.append([nums[t], t])
                            seen.add(t)
                        i += 1

                min_jumps += 1
            return min_jumps
        

        
        return bfs(nums)


        
        

       
                    
                