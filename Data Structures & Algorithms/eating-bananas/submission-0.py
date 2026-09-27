class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        min_value = 0
        last_valid_val = 0
        while left <= right:
            middle = (left + right) // 2
            count = 0
            for i in range(len(piles)):
                if middle > piles[i]:
                    count += 1
                elif piles[i] % middle == 0:
                    count += (piles[i] // middle)
                else:
                    count += (piles[i] // middle) + 1
            if count > h:
                left = middle + 1
            elif count <= h:
                last_valid_val = middle
                right = middle - 1           
        return last_valid_val
        
        
            

        