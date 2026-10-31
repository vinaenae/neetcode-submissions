class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res, count = [intervals[0]], 0
        for s, f in intervals[1:]:
            last = res[-1][1]
            if f < last:
                res[-1] = [s, f]
                count += 1
            elif s < last:
                count += 1
            else:
                res.append([s, f])
        return count
        






        