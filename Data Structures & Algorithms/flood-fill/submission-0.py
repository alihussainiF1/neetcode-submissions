class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        from collections import deque
        visit = set()
        queue = deque()

        ROWS, COL = len(image), len(image[0])
        if image[sr][sc] == color:
            return image
        queue.append((sr,sc))
        visit.add((sr,sc))
        original_color = image[sr][sc]

        while queue:
            for i in range(len(queue)):
                s_r,s_c = queue.popleft()
                image[s_r][s_c]=color
                dir = [[0,1],[0,-1],[-1,0],[1,0]]
                for x,y in dir:
                    new_x, new_y = s_r + x , s_c + y 

                    if min(new_x,new_y) < 0 or new_x == ROWS or new_y == COL or (new_x,new_y) in visit or image[new_x][new_y] != original_color:
                        continue
                    visit.add((new_x,new_y))
                    queue.append((new_x,new_y))
                    image[new_x][new_y] = color 

        return image

