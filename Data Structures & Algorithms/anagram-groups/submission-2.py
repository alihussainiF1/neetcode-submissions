class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct ={}
        res = []
        def _convert_to_strlist(s:str)->str:
            l = 'abcdefghijklmnopqrstuvwxyz'
            arr_char = [0]*26
            dct_char={}
            i = 0 
            for c in l:
                if c not in dct_char:
                    dct_char[c]= i
                    i+=1
            for c in s:
                arr_char[dct_char[c]]+=1
            return arr_char

        char_key = str(_convert_to_strlist(strs[0]))
        print(char_key,type(char_key))

        for c in strs:
           char_key = str(_convert_to_strlist(c))
           if char_key not in dct: 
            dct[char_key] = [c]
           else:
            dct[char_key].append(c)
        print(dct)

        res = [x for x in dct.values()]
        return res


