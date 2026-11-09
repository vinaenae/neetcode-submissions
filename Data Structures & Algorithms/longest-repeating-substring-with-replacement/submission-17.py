class Solution:
    def characterReplacement(self, s: str, k: int) -> int:



        l, size, m_size = 0, 0, 0
        hash = {}
        for r in range(len(s)):
            hash[s[r]] = 1 + hash.get(s[r], 0)
            if not (r - l + 1) - max(hash.values()) <= k:
                hash[s[l]] -= 1
                l += 1
            m_size = max(m_size, r - l + 1)
        return m_size
