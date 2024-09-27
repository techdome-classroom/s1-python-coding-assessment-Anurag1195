class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        #if the grid is empty , return 0 islands
        if not grid or not grid[0]:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range (rows)]

        def dfs(r , c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 
            if visited[r][c] or grid[r][c] == 'W':
                return

            visited[r][c] = True

            dfs(r+1 , c) 
            dfs(r-1 , c)
            dfs(r , c+1)
            dfs(r , c-1)

        island_count = 0

        for r in range (rows):
            for c in range (cols):
                            
        return 0
