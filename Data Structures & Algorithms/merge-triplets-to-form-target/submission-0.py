class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        first = target[0]
        second = target[1]
        third = target[2]

        copy = []
        for i, (f, s, t) in enumerate(triplets):
            if f <= first and s <= second and t <= third:
                copy.append([f, s, t])

        newFirst, newSecond, newThird = False, False, False
        for f, s, t in copy:
            if f == first:
                newFirst = True
            if s == second:
                newSecond = True
            if t == third:
                newThird = True
        return newFirst and newSecond and newThird
        