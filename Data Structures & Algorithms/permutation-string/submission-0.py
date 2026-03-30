class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target_count = [0] * 26 # Character counts of s1
        window_count = [0] * 26 # character count of the current sliding window in s2 (of size len(s1))
        for c in s1:
            target_count[ord(c) - ord('a')] += 1
        for i in range(len(s2)):
            window_count[ord(s2[i]) - ord('a')] += 1
            if i >= len(s1):
                window_count[ord(s2[i - len(s1)]) - ord('a')] -= 1
            if target_count == window_count:
                return True
        return False