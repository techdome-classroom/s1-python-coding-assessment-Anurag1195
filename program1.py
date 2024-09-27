class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        #if the grid is empty , return 0 islands
        if not grid or not grid[0]:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False For _ in range (cols)] for _ in range(rows)]

                    
        return 0
