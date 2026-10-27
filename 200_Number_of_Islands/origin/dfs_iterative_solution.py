"""
Iterative DFS solution for a Number of Islands problem.
"""
from collections import deque


class Solution:
    def numIslands(self, grid):
        numIslands = 0
        for rowIdx, rowArr in enumerate(grid):
            for colIdx, cellVal in enumerate(rowArr):
                if cellVal == "1":
                    stack = deque([(rowIdx, colIdx)])
                    while stack:
                        curRowIdx, curColIdx = stack.pop()
                        if (curRowIdx < 0 or curRowIdx >= len(grid)
                                or curColIdx < 0 or curColIdx >= len(grid[0]) or grid[curRowIdx][curColIdx] != "1"):
                            continue
                        grid[curRowIdx][curColIdx] = "0"
                        stack.append((curRowIdx - 1, curColIdx))
                        stack.append((curRowIdx + 1, curColIdx))
                        stack.append((curRowIdx, curColIdx - 1))
                        stack.append((curRowIdx, curColIdx + 1))
                    numIslands += 1
        return numIslands


print(Solution().numIslands([['1', '1', '0', '1', '0', '1', '1']]))
