import collections
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS,COLS=len(grid),len(grid[0])

        visited=set()
        count=0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]=='1' and (i,j) not in visited:
                    q=collections.deque()
                    q.append([i,j])
                    visited.add((i,j))
                    while q:
                        x,y=q.popleft()

                        for r,c in [[0,1],[0,-1],[1,0],[-1,0]]:
                            new_r,new_c=x+r,y+c
                            if 0<=new_r<ROWS and 0<=new_c<COLS and (new_r,new_c) not in visited and grid[new_r][new_c]!='0':
                                q.append([new_r,new_c])
                                visited.add((new_r,new_c))
                    count+=1
        return count

