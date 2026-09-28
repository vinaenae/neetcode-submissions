class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash, hash2 = {}, {}
        l, r = 0, 0

        for i in range(len(s1)):
            hash[s1[i]] = 1 + hash.get(s1[i], 0)

        while r < len(s2):

            # character isn't even allowed
            if s2[r] not in hash:
                hash2 = {}
                r += 1
                l = r
                continue

            # add current character
            hash2[s2[r]] = 1 + hash2.get(s2[r], 0)

            # too many copies of current character
            while hash2[s2[r]] > hash[s2[r]]:
                hash2[s2[l]] -= 1
                l += 1

            # valid window has same length as s1
            if (r - l + 1) == len(s1):
                return True

            r += 1

        return False