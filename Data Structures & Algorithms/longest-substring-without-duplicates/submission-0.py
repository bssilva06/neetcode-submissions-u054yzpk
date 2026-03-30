class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        R = 0
        count = 0
        seen = set()
        while R < len(s):
            if s[R] not in seen:
                seen.add(s[R])
                R += 1
                count = max(count, len(seen))
            else:
                seen.remove(s[L])
                L += 1
        return count