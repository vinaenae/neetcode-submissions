class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        new = set()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            first = nums[i]
            new_lst = nums[0:i] + nums[i+1:]
            left = 0
            right = len(new_lst) - 1
            while right > left:
                if first + new_lst[left] + new_lst[right] == 0:
                    if tuple(sorted([nums[i], new_lst[left], new_lst[right]])) not in new:
                        new.add(tuple(sorted([nums[i], new_lst[left], new_lst[right]])))
                        output.append([nums[i], new_lst[left], new_lst[right]])
                    left += 1
                    right -=1 
                if first + new_lst[left] + new_lst[right] < 0:
                    left += 1
                elif first + new_lst[left] + new_lst[right] > 0:
                    right -= 1
        return output

        



       



        