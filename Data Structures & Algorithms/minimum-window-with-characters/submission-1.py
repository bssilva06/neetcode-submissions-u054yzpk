class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = {}
        need = len(set(t))
        have = 0
        L = 0
        window_map = {}
        res = [-1, -1]
        resLen = float("inf")
        for c in t:
            if c in countT:
                countT[c] += 1
            else:
                countT[c] = 1
        for R in range(len(s)):
            if s[R] in window_map:
                window_map[s[R]] += 1
            else:
                window_map[s[R]] = 1
            if s[R] in countT and countT[s[R]] == window_map[s[R]]:
                have +=1
            while have == need:
                if (R - L + 1) < resLen:
                    res = [L, R]
                    resLen = (R - L + 1)
                window_map[s[L]] -= 1
                if s[L] in countT and countT[s[L]] > window_map[s[L]]:
                    have -= 1
                L += 1
        if resLen == float("inf"):
            return ""
        else:
            return s[res[0]:res[1]+1]