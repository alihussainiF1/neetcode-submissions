class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {}
        for i in nums:
            if i not in dct:
                dct[i] = 1
            else:
                dct[i]+=1
        res = []
        for i,v in dct.items():
            res.append((v,i))
        res.sort(reverse=True)
        
        final = []
        j = 0 
        print(dct)
        for i in range(k):
            _,a = res[j]
            j += 1
            final.append(a)
        return final
            