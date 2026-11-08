class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            if nums[i] not in hash:
                hash[nums[i]] = i

        for i in range(len(nums)):
            other = target - nums[i]
            if other in hash:
                if i != hash[other]:

                    return [min(i, hash[other]), max(i, hash[other])]
        

                
        # l = 0
        # converted = set(nums)
        # for i in range(len(nums)):
        #     if target - nums[i] in converted:
        #         found = nums.index(target - nums[i])
        #         if i == found:
        #             continue
        #         order = sorted((i, found))
        #         return order

        
        
        
            


        