class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_alpha = {}

        s = 'abcdefghijklmnopqrstuvwxyz'
        i = 0
        for c in s:
            map_alpha[c] = i
            i +=1
        print(map_alpha)
        dct = {}
        for s in strs:
            tmp = []
            for c in s:
                tmp.append(map_alpha[c])
            tmp.sort()
            str_t = [str(x) for x in tmp]
            sort_tmp = ''.join(str_t)
            if sort_tmp not in dct:
                dct[sort_tmp] = [s]
            else:
                dct[sort_tmp].append(s)
        res = [] 
        for items in dct.values():
            res.append(items)
        return res

