class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dct_s = {}
        dct_t = {}

        for c in s:
            if c not in dct_s:
                dct_s[c] = 1
            else:
                dct_s[c] += 1

        for c in t:
            if c not in dct_t:
                dct_t[c] = 1
            else:
                dct_t[c] += 1
        
        return dct_s == dct_t
        