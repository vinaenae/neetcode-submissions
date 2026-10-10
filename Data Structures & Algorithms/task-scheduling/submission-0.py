class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        minHeap = [-n for n in counts.values()]
        heapq.heapify(minHeap)
        q = deque()

        time = 0
        while minHeap or q:
            if minHeap:
                if minHeap[0] == -1:
                    heapq.heappop(minHeap)
                else:
                    q.append([1 + heapq.heappop(minHeap), time + n])
            
            if q:
                if time == q[0][1]:
                    heapq.heappush(minHeap, q.popleft()[0])
            
            time += 1
        return time
            







        