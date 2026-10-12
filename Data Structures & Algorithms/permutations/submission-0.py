class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(i, nums):
            if i == len(nums):
                return [[]]
            
            perms = dfs(i+1, nums)
            res = []

            for p in perms:
                for c in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(c, nums[i])
                    res.append(pCopy)
            return res
        return dfs(0, nums)
                
            


        
        
        