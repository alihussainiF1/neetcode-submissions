class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res =[] 
        s=''
        def dfs(s,openN,closedN):
            if openN == n and closedN == n:
                res.append(s)
                
            if openN <n:
           
                dfs(s+'(',openN+1,closedN)
            if closedN <openN:
                dfs(s+')',openN,closedN+1)
        
        dfs('',0,0)
        return res