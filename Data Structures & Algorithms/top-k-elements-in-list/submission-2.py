class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for number in nums:
            if number not in counts:
                counts[number] = 1
            else:
                counts[number] += 1
        lst = sorted(list(counts.values()), reverse = True)
        largest = lst[0:k]
        largest_keys = []
        for key, value in counts.items():
            if value in largest:
                largest_keys.append(key)
        return largest_keys

            
        