class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        new_dict = Counter(nums)
        values = sorted(new_dict, key=lambda item: -new_dict[item])
        return values[:k]    




            
        