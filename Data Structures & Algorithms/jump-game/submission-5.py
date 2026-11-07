class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        post = len(nums) - 1
        for i in range(len(nums) - 2, -1 ,- 1):
            if nums[i] + i >= post:
                post = i
        return True if post == 0 else False























        # # i = 0
        # # while i < len(nums) and i != len(nums) -1:
        # #     if nums[i] == 0:
        # #         return False
        # #     i += nums[i]
        # # return True
    
        # # curSum = nums[0]
        # # maxSum = nums[0]

        # # for i in range(1, len(nums)):
        # #     if maxSum == len(nums):
        # #         return True
            
        # #     curSum = max(curSum, 0)
        # #     curSum += nums[i]
        # #     maxSum = max(curSum, maxSum)
        # post = len(nums) - 1
        # for i in range(len(nums) -2, -1, -1):
        #     if i + nums[i] >= post:
        #         post = i
        # return True if post == 0 else False
            





            
        