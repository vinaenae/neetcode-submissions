import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances, ans = [], []
        for i in range(len(points)):
            curr = math.sqrt((points[i][0])**2 + ((points[i][1])**2))  
            distances.append((curr, points[i]))
        heapq.heapify(distances)
        n = 0
        while n < k:
            ans.append(distances[0][1])
            heapq.heappop(distances)
            n += 1
        return ans


        
        