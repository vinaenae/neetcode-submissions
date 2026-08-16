class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for c in s:
            if c.isalnum():
                new_str += c
        new_str = new_str.lower()
        j = 0
        r = len(new_str) -1
        while r > j:
            if new_str[j] != new_str[r]:
                return False
            j += 1
            r -= 1
        return True

        