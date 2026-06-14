class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        s = sorted(s)
        t = sorted(t)
        print(s[0],t[0])
        return s==t