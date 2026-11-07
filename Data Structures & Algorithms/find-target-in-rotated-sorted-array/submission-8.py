class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1

        l, r = 0, len(nums) -1 
        while l <= r:
            middle = (l + r) // 2
            if target < nums[middle] and target < nums[l]:
                l = middle + 1
            elif target < nums[middle] and target > nums[l]:
                r = middle - 1
            elif target > nums[middle] and target > nums[r]:
                r = middle - 1
            elif target > nums[middle] and target < nums[l]:
                l = middle + 1
            else:
                return nums[middle]
        return -1

                


        