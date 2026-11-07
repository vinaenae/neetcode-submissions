class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        differences = [gas[i] - cost[i] for i in range(len(gas))]
    
        curSum, minIndex = 0, float("inf")
        for i in range(len(differences)):
            curSum += differences[i]
            if curSum >= 0:
                minIndex = min(minIndex, i)
            else:
                minIndex = float("inf")
                curSum = 0
        return minIndex if minIndex != float("inf") else -1


