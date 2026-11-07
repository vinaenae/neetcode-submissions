"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        if len(intervals) == 1:
            return 1
        
        intervals = sorted(intervals, key = lambda item: item.start)
        heap = [intervals[0].end]
        count = 1
        for i in range(1, len(intervals)):
            if intervals[i].start < heap[0]:
                count += 1
            else:
                heapq.heappop(heap)
            heapq.heappush(heap, intervals[i].end)
        return count
            
             


        
        