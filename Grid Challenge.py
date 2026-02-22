def gridChallenge(grid):
    # 1. Sort แต่ละแถว
    sorted_grid = ["".join(sorted(row)) for row in grid]
    
    # 2. เช็คแต่ละหลัก (Column)
    rows = len(sorted_grid)
    cols = len(sorted_grid[0])
    
    for c in range(cols):
        for r in range(rows - 1):
            if sorted_grid[r][c] > sorted_grid[r+1][c]:
                return "NO"
    return "YES"