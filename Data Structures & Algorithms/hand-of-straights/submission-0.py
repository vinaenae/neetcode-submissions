import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counter = Counter(hand)
        arr = list(counter.keys())
        heapq.heapify(arr)

        while arr:
            first = arr[0]
            for i in range(first, first + groupSize):
                if i not in counter:
                    return False
                counter[i] -= 1
                if counter[i] == 0:
                    if i != arr[0]:
                        return False
                    heapq.heappop(arr)
        return True          



        