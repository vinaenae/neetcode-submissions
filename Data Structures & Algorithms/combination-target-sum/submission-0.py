class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.group_split = []
        def backtrack(start, curr_spl, sum):
            if sum == target:
                self.group_split.append(curr_spl.copy())
                return
            
            if sum > target:
                return
                
            for i in range(start, len(nums)):
                    curr_spl.append(nums[i])
                    backtrack(i, curr_spl, sum + nums[i])
                    curr_spl.pop()
        backtrack(0, [] ,0)
        return self.group_split

        
        