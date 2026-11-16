class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp, longest = [1] * len(nums), 1
        for i in range(len(nums) - 1, -1, -1):
            longest = 1
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    longest = max(longest, 1 + dp[j])
            dp[i] = longest
        return max(dp)