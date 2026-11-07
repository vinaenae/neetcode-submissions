class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        for i, (start, end) in enumerate(intervals):
            if start > newInterval[1]:
                output.append(newInterval)
                return output + intervals[i:]
            if newInterval[0] > end:
                output.append([start, end])
            else:
                newInterval[0] = min(start, newInterval[0])
                newInterval[1] = max(end, newInterval[1])
        output.append(newInterval)
        return output
        






        # output = []
        # in_start = newInterval[0]
        # our_end = newInterval[1]

        # if not intervals:
        #     return [newInterval]


        # if our_end < intervals[0][0]:
        #     output = intervals.copy()
        #     output.insert(0, newInterval)
        #     return output
        
        # if in_start > intervals[-1][1]:
        #     output = intervals.copy()
        #     output.append(newInterval)
        #     return output

        # output = intervals.copy()
        # for i, (start, end) in enumerate(output):
        #     if our_end < start:
        #         output.insert(i, newInterval)
        #         break
        #     if in_start <= end:
        #         output[i] = [min(start, in_start), max(end, our_end)]
        #         break
        
        
        # new_output = [output[0]]
        # for start, end in output[1:]:
        #     last = new_output[-1][1]
        #     if start <= last:
        #         new_output[-1][1] = max(last, end)
        #     else:
        #         new_output.append([start, end])
        
        # return new_output


            