"""
Recursive DFS solution for a Number of Islands problem.
"""

class Solution:
    def dfs(self, grid, rowIdx, colIdx):
        if rowIdx < 0 or rowIdx >= len(grid) or colIdx < 0 or colIdx >= len(grid[0]) or grid[rowIdx][colIdx] != "1":
            return

        grid[rowIdx][colIdx] = "0"
        self.dfs(grid, rowIdx - 1, colIdx)
        self.dfs(grid, rowIdx + 1, colIdx)
        self.dfs(grid, rowIdx, colIdx - 1)
        self.dfs(grid, rowIdx, colIdx + 1)

    def numIslands(self, grid: list[list[str]]) -> int:
        numIslands = 0
        for rowIdx, rowArr in enumerate(grid):
            for colIdx, cellVal in enumerate(rowArr):
                if cellVal == "1":
                    self.dfs(grid, rowIdx, colIdx)
                    numIslands += 1
        return numIslands