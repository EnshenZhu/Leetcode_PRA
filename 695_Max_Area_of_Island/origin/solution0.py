class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        def dfs(row, col, curArea=0):
            if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]):
                if grid[row][col] == 1:
                    grid[row][col] = 0  # turn it into zero be prevent duplicated traverse
                    curArea += 1
                    curArea = dfs(row + 1, col, curArea=curArea)
                    curArea = dfs(row - 1, col, curArea=curArea)
                    curArea = dfs(row, col + 1, curArea=curArea)
                    curArea = dfs(row, col - 1, curArea=curArea)
            return curArea

        if not grid:
            return 0

        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    curArea = dfs(row=i, col=j)
                    maxArea = max(maxArea, curArea)
        return maxArea


print(Solution().maxAreaOfIsland(grid=[[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                     [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                                     [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))
