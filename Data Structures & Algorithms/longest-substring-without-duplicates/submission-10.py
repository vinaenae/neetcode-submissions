class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, longest, r, curr_len = 0, 0, 0, 0
        hash = set()
        while r < len(s):
            if s[r] not in hash:
                hash.add(s[r])
                curr_len += 1
                ref = curr_len
                r += 1
            else:
                hash.remove(s[l])
                l += 1
                curr_len -= 1
            longest = max(ref, longest)
        return longest
        