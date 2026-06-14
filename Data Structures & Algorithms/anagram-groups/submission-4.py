class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dct = {} 

        for i in strs:
            st = ''.join(sorted(i))
            print(st)
            if st in dct:
                dct[st].append(i)
            else:
                dct[st] = [i]
        print(dct)
        res = [] 
        for i in dct.values():
            res.append(i)
            print(i)
        return res