class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #sliding window technique with l,r at 0 
        #window size - max_freq of chars until now <= k

        max_freq,ret=0,0
        l,r=0,0
        char_count={}
        for r in range(len(s)):
            char_count[s[r]] = char_count.get(s[r],0)+1
            max_freq = max(max_freq,char_count[s[r]])
            while ((r-l+1)-max_freq > k):
                char_count[s[l]]-=1
                l+=1
            ret = max(ret,r-l+1)
        return ret

