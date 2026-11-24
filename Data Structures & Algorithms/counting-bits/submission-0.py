class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [i for i in range(n+1)]
        for i in range(len(output)):
            count = 0
            while output[i]:
                if output[i] % 2 == 1:
                    count += 1
                output[i] = output[i] >> 1
            output[i] = count
        return output

