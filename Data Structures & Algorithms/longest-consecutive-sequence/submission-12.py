class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        nums.sort()
        print(nums)
        l = 0
        longest = 1
        s = {nums[0]}
        for r in range(1, len(nums)):
            if nums[r] != 1 + nums[r - 1]:
                if nums[r] in s:
                    continue
                else:
                    l = r
                    s.clear()
            s.add(nums[r])
            longest = max(longest, len(s))
        return longest
                
        



        



        