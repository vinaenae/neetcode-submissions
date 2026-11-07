import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances, output = [], []
        for i in range(len(points)):
            x, y = points[i]
            distance = x**2 + y**2
            heapq.heappush(distances, [distance, points[i]])
        for i in range(k):
            res = heapq.heappop(distances)
            output.append(res[1])
        return output


        
           


        
        