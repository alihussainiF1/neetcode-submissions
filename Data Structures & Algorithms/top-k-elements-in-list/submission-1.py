class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {}

        for i in nums:
            if i not in dct :
                dct[i] = 1
            else :
                dct[i]+=1
        print(dct)

        res =[]

        for i in dct:
            res.append((dct[i],i))
        res.sort()
        print(res)
        final = []
        for j in range(k):
            _,x= res.pop()
            final.append(x)

        return final

 