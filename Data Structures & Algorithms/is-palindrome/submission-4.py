class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s_list=[]
        for c in s:
            if c.isalnum():
                s_list.append(c)
        print(s_list)
        return s_list == s_list[::-1]
