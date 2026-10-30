import heapq
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # ref = {char for char in t}
        # L, shortest, curr = 0, float("inf"), []
        # heap = []
        # char_count = len(t)
        # for R in range(len(s)):
        #     if s[R] not in ref and curr:
        #         curr.append(s[R])
        #     elif s[R] not in curr and s[R] not in ref:
        #         curr.append((s[R]))
        #         char_count -= 1
        #     elif char_count == 0:
        #         shortest = min(shortest, R - L + 1)
        #         heap.heappush((curr, shortest))
        #         L = R
        #         curr.clear()
        #         char_count = len(t)
        #     else:
        #         L += 1
        # return heap[0][0]

        if t == "": return ""

        countT, window = Counter(t), {}

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("inf")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""
        
    #     ref = Counter(t)
    #    curr = defaultdict(int)
    #     lst = []
    #     for R in range(len(s)):
    #         lst.append(s[R])
    #         if count == len(ref):
    #             if curr > ref:
    #                 shortest = 
    #         if s[R] in ref:
    #             curr[R] += 1
    #             count += 1
            

