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
        count = 1
        intervals.sort(key = lambda item: item.start)

        arr = []
        heapq.heappush(arr, intervals[0].end)
        for i in intervals[1:]:
            if i.start < arr[0]:
                count += 1
            elif i.start >= arr[0]:
                heapq.heappop(arr)
            heapq.heappush(arr, i.end)
        return count

        
        