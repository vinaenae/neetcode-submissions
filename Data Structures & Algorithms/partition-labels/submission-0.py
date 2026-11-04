class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i in range(len(s) -1, -1, -1):
            if s[i] not in lastIndex:         
                lastIndex[s[i]] = i
        
        start, end, output = 1, 0, []
        for i in range(len(s)):
            end = max(lastIndex[s[i]], end)
            if i == end:
                output.append(start)
                start = 1
            else:
                start += 1
        return output
        