class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, curr, longest = 0, 0, 0
        hash = {}
        for r in range(len(s)):
            hash[s[r]] = 1 + hash.get(s[r], 0)
            if ((r - l + 1) - max(hash.values())) > k:
                hash[s[l]] -=1
                l += 1
            else:
                curr += 1
            longest = max(longest, curr)
        return longest


        
            









