class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        visit = set()
        for i in range(len(nums)):
            if nums[i] not in visit:
                visit.add(nums[i])
            else:
                return nums[i]
        

            
        