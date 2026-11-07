import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap, -(nums[i]))
        i = 0
        while i < k-1:
            heapq.heappop(heap)
            i += 1
        return -heap[0]

        
        
        