class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dct_s, dct_t = {} , {}

        for i in s:
            if i in dct_s:
                dct_s[i]+=1
            else:
                dct_s[i] = 1
        
        for j in t:
            if j in dct_t:
                dct_t[j]+=1
            else:
                dct_t[j]=1
        return dct_t == dct_s
