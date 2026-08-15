class Solution:
    import heapq
    def longestConsecutive(self, nums: List[int]) -> int:   
        heap = list(set(nums.copy()))
        heapq.heapify(heap)
        if len(nums) > 1:
            curr_lst = [heapq.heappop(heap)]
            counter = 1
            longest_count = 1
            for i in range(len(heap)):
                if (heap[0] - curr_lst[-1]) == 1:
                    curr_lst.append(heapq.heappop(heap))
                    counter += 1
                    if counter > longest_count:
                        longest_count = counter
                else:
                    counter = 1
                    curr_lst = [heapq.heappop(heap)]
            return longest_count
        elif len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1



        