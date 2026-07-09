class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = [] 

        for i in s:
            i = i.lower()
            if i.isalnum():
                temp.append(i)
        print(temp)

        l = len(temp)
        i,j= 0, len(temp)-1

        if l%2==0:
            while i<=j:
                print(i,j)
                if temp[i]!=temp[j]:
                    return False
                else:
                    i+=1
                    j-=1
        else:
            while i<j:
                print(i,j)
                if temp[i]!=temp[j]:
                    return False
                else:
                    i+=1
                    j-=1
        return True


        #return temp == temp[::-1]