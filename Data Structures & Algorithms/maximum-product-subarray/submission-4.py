class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax, curMin = 1, 1

        for i in range(len(nums)):
            if nums[i] == 0:
                curMax, curMin = 1, 1
                continue
            tmp = curMax * nums[i]
            curMax = max(nums[i] * curMax, nums[i] * curMin, nums[i])
            curMin = min(tmp, nums[i] * curMin, nums[i])
            res = max(res, curMax)
        return res
        # if len(nums) == 1:
        #     return nums[-1]
        # maxSum = curSum = float("-inf")
        # cur = set()
        # for i in range(len(nums)):
        #     cur.add(nums[i])
        #     if len(cur) > 1:
        #         curSum = max(curSum, 1)
        #         curSum *= nums[i]
        #     else:
        #         curSum = 1
        #         curSum *= nums[i]
        #     maxSum = max(curSum, maxSum)
        # return maxSum
        