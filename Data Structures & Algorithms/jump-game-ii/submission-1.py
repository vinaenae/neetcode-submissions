from collections import deque
class Solution:
    def jump(self, nums: List[int]) -> int:
        # post = len(nums) - 1
        # curr_steps = 0
        # cur_sum = nums[0]
        # for i in range(len(nums)):
        #     cur_sum = max(cur_sum, 0)
        #     curr_sum += nums[i]

        #     if i + nums[i] >= post:
        #         min_value = min(min_value, curr_steps)
        #     curr_steps
        if len(nums) == 1:
            return 0

        level = 0
        queue = deque([0])
        visit = {0}

        while queue:
            level += 1
            for _ in range(len(queue)):
                idx = queue.popleft()
                c = 1
                while c <= nums[idx]:
                    nxt = idx + c
                    if nxt >= len(nums) - 1:
                        return level
                    if nxt not in visit:
                        visit.add(nxt)
                        queue.append(nxt)
                    c += 1
        return level
                    
                