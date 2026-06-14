from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adj_list = {i: [] for i in range(n)}
        
        # Building the adjacency list
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        def dfs(node):
            stack = [node]
            while stack:
                curr = stack.pop()
                if curr not in visited:
                    visited.add(curr)
                    for nei in adj_list[curr]:
                        if nei not in visited:
                            stack.append(nei)
        
        res = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
        return res
