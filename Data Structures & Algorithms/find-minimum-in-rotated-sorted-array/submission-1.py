class Solution:
    def findMin(self, nums: List[int]) -> int:
        #rotations = 0
        #b = []
        #for num in nums:
        #    if num != 0:
        #        rotations += 1
        #        b.append(num)
        #    else:
        #        nums.extend(b)
        #        break
        left = 0
        right = len(nums) - 1
        while left < right:
            middle = (left + right) // 2
            if nums[middle] > nums[right]:
                left = middle + 1
            elif nums[middle] < nums[right]:
                right = middle
        return nums[(left + right) // 2]



        