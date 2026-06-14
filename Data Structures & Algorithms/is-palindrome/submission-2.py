class Solution:
    def isPalindrome(self, s: str) -> bool:

        pal_list = []
        for c in s:
            if c in ['0','1','2','3','4','5','6','7','8','9']:
                pal_list.append(c)
            elif ord('a') <= ord(c.lower()) <= ord('z'):
                pal_list.append(c.lower())
        s1=''.join(pal_list)
        s2=''.join(pal_list[::-1])

        return s1==s2