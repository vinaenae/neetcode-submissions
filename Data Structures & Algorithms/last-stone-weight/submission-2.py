import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        weights = [-x for x in stones]
        heapq.heapify(weights)
        while len(weights) >= 2:
            x = -(heapq.heappop(weights))
            y = -(heapq.heappop(weights))
            if x < y:
                heapq.heappush(weights, -(y - x))
                continue
            if x > y:
                heapq.heappush(weights, -(x - y))
        return -weights[0] if weights else 0



