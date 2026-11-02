class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        if len(gas) == 1:
            return 0
        diff = [x - y for x, y in zip(gas, cost)]
        curSum = 0

        minIndex = 0
        print(diff)

        for i in range(len(diff)):
            curSum = max(curSum, 0)
            curSum += diff[i]
            if curSum >= 0:
                minIndex = min(minIndex, i)
            else:
                minIndex = float("inf")
        return minIndex if minIndex != float("inf") else -1
     