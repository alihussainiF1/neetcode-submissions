class Solution:
    def isPalindrome(self, s: str) -> bool:

        temp=[]
        for i in s:
            if ord('a')<=ord(i.lower())<=ord('z') or ord('0')<=ord(i.lower())<ord('9'):
                temp.append(i.lower())

        l,r=0,len(temp)-1
        print(s)
        while(l<=r):
            if temp[l]==temp[r]:
                l+=1
                r-=1
            else:
                return False
        return True 