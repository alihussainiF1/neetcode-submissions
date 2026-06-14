class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        island = 0 
        visit = set()
        def bfs(r,c):
            queue = deque()
            queue.append((r,c))
            visit.add((r,c))

            while queue:
                r,c = queue.popleft()
                for dr,dc in [[0,1],[1,0],[-1,0],[0,-1]]:
                    new_r, new_c = r+dr, c+dc

                    if rows<=new_r or new_r<0 or cols<=new_c or new_c<0:
                        continue
                    if grid[new_r][new_c] == '0' or ((new_r,new_c)) in visit:
                        continue
                    queue.append((new_r,new_c))
                    visit.add((new_r,new_c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visit:
                    bfs(r,c)
                    island +=1

        return island
        