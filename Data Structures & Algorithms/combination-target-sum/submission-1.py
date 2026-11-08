class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        global_list = []
        def dfs(temp, i, sum):
            if i == len(nums) or sum > target:
                return
            if sum == target:
                global_list.append(temp.copy())
                return
            
            
            temp.append(nums[i])

            sum += nums[i]

            dfs(temp, i, sum)

            temp.pop()

            sum -= nums[i]

            dfs(temp, i + 1, sum)
        dfs([], 0, 0)
        return global_list

        
        