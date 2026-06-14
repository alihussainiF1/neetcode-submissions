class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited=set()
        adj_list={}
        for a,b in edges:
            if a not in adj_list:
                adj_list[a]=[b]
            else:
                adj_list[a].append(b)
            if b not in adj_list:
                adj_list[b]=[a]
            else:
                adj_list[b].append(a)
        
        for i in range(n):
            if i not in adj_list:
                adj_list[i]=[]
        
        def dfs(i):
            stack=[i]
            while stack:
                curr=stack.pop()
                if curr not in visited:
                    visited.add(curr)
                    for neighbour in adj_list[curr]:
                        if neighbour not in visited:
                            stack.append(neighbour)
        
        res=0
        for i in range(n):
            if i not in visited:
                dfs(i)
                res+=1
        return res
