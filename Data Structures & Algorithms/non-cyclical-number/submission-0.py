class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        sum = float("inf")
        output = n
        while output != 1:
            if output in visit:
                return False
            
            visit.add(output)

            sum = 0
            while output:
                sum += (output % 10) ** 2
                output = output // 10
            output = sum
        return True
            
            
        