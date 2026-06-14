class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1
        a,b = 1,1 
        if n == 1 or n ==2:
            print('h')
            return n
        for i in range(2,n+1):
            temp = a + b 
            a = b 
            b = temp 
            dp[i] = dp[i-1] + dp[i-2]
        print(dp)
        return b