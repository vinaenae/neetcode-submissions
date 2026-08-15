class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = defaultdict(list)
        for i, num in enumerate(nums):
            s[num] = i
        for i in range(len(nums)):
            if (target - nums[i]) in s:
                j = s[target - nums[i]]
                if i < j:
                    return [i, j]
                if j < i:
                    return [j, i]
                
        
        
        
            


        