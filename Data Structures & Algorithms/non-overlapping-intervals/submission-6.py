class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0
        
        sorted_ints = sorted(intervals, key=lambda item: item[0])
        count = 0
        end = sorted_ints[0][1]
        for s, e in sorted_ints[1:]:
            if s < end:
                count += 1
                end = min(end, e)
            else:
                end = e
            
        return count

        






        