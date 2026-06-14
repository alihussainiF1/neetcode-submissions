class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict= [0]*26
        t_dict= [0]*26

        for c in s:
            s_dict[ord(c)-ord('a')]+=1
        for c in t:    
            t_dict[ord(c)-ord('a')]+=1
        print(t_dict,s_dict)
        return t_dict==s_dict
