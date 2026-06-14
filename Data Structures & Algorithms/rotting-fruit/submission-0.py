class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS,COLS=len(grid),len(grid[0])
        fruits,time=0,0
        q=collections.deque()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==1:
                    fruits+=1
                if grid[i][j]==2:
                    q.append([i,j])
        while q and fruits >0:
            for i in range(len(q)):
                x,y=q.popleft()
                for r,c in [[0,1],[1,0],[-1,0],[0,-1]]:
                    new_r,new_c=x+r,y+c
                    if 0<=new_r<ROWS and 0<=new_c<COLS and grid[new_r][new_c]==1:
                        grid[new_r][new_c]=2
                        q.append([new_r,new_c])
                        fruits-=1
            time+=1
        return time if fruits==0 else -1
