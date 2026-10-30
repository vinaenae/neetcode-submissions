class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        output = []
        in_start = newInterval[0]
        our_end = newInterval[1]

        if not intervals:
            return [newInterval]


        if our_end < intervals[0][0]:
            output = intervals.copy()
            output.insert(0, newInterval)
            return output
        
        if in_start > intervals[-1][1]:
            output = intervals.copy()
            output.append(newInterval)
            return output

        output = intervals.copy()
        for i, (start, end) in enumerate(output):
            if our_end < start:
                output.insert(i, newInterval)
                break
            if in_start <= end:
                output[i] = [min(start, in_start), max(end, our_end)]
                break
        
        
        new_output = [output[0]]
        for start, end in output[1:]:
            last = new_output[-1][1]
            if start <= last:
                new_output[-1][1] = max(last, end)
            else:
                new_output.append([start, end])
        
        return new_output


            