class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSquare(n):
            s=0
            while n:
                s+=(n%10)**2
                n//=10
            return s
        
        visited = set()
        while n not in visited:
            visited.add(n)
            n = sumOfSquare(n)

            if n == 1 :
                return True 
        return False
        
