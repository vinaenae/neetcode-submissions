class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.group_split = []
        def backtrack(i, curr_spl):
                if i == len(nums):
                    self.group_split.append(curr_spl.copy())
                    return
                
                curr_spl.append(nums[i])
                backtrack(i + 1, curr_spl)

                curr_spl.pop()

                backtrack(i + 1, curr_spl)
        curr_spl = []
        backtrack(0, curr_spl)
        return self.group_split


        