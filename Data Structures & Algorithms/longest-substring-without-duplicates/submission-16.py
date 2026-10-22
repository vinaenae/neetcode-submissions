class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, vals, count, longest = 0, set(), 0, 0
        for i in range(len(s)):
            while s[i] in vals:
                vals.remove(s[left])
                left += 1
                count -= 1
            vals.add(s[i])
            count += 1
            longest = max(longest, count)

        return longest
        # while left < len(s):
        #     count = 0
        #     for i in range(left, len(s)):
        #         if s[i] not in vals:
        #             vals.add(s[i])
        #             count += 1
        #         else:
        #             vals.remove(s[i])
        #             left += 1
        #         longest = max(longest, count)
        # return longest 


        