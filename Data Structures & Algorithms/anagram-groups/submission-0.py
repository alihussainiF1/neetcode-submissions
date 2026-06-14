class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct={}
        for word in strs:
            k=''.join(sorted(word))

            if k in dct:
                dct[k].append(word)
            else:
                dct[k] = [word]
        res=[]
        for i in dct:
            res.append(dct[i])
        return res 