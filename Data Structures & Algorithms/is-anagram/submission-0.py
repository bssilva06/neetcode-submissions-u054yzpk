class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_map = {}

        for c in s:
            if c in hash_map:
                hash_map[c] += 1
            else:
                hash_map[c] = 1
        
        for c in t:
            if c in hash_map:
                hash_map[c] -= 1
                if hash_map[c] == 0:
                    del hash_map[c]
            else:
                return False
        return True
        

        