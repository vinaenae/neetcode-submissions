class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_chars_s = {}
        count_chars_t = {}
        for n in s:
            if n not in count_chars_s:
                count_chars_s[n] = 1
            else:
                count_chars_s[n] += 1
        for c in t:
            if c not in count_chars_t:
                count_chars_t[c] = 1
            else:
                count_chars_t[c] += 1
        print(count_chars_s)
        print(count_chars_t)
        if count_chars_s == count_chars_t:
            return True
        return False
        
        