class Solution(object):
    def numIslands(self, grid):
        ROWS, COLS = len(grid), len(grid[0])


        visted = set()
        islands = 0
        for row in range(ROWS):
            for col in range(COLS):

                if grid[row][col] == "1" and (row,col) not in visted:

                    q = deque()
                    q.append((row,col))
                    visted.add((row,col))

                    while q:

                        x,y = q.popleft()
    


                        neighbors = [
                            [x+1,y],
                            [x-1,y],
                            [x,y+1],
                            [x,y-1]
                        ]

                        for nr, nc in neighbors:
                            if 0 <= nr < ROWS and 0 <= nc < COLS and (nr,nc) not in visted and grid[nr][nc] == "1":
                                q.append((nr,nc))
                                visted.add((nr,nc))
                        

                    islands +=1
        return islands
        
