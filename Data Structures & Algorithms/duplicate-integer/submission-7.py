class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list_count = {}
        for n in nums:
            if n not in list_count:
                list_count[n] = 1
            else:
                list_count[n] += 1
        for key, value in list_count.items():
            if value > 1:
                return True
        return False
