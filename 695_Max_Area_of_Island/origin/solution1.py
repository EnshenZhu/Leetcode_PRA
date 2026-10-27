from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        maxArea = 0
        for rowIdx, rowArr in enumerate(grid):
            for colIdx, val in enumerate(rowArr):
                if val:
                    curArea = 0
                    stack = deque([(rowIdx, colIdx)])
                    while stack:
                        curRowIdx, curColIdx = stack.pop()
                        grid[rowIdx][colIdx] = 0
                        curArea += 1
                        for neighborRow, neighborCol in (
                                (curRowIdx + 1, curColIdx),
                                (curRowIdx - 1, curColIdx),
                                (curRowIdx, curColIdx + 1),
                                (curRowIdx, curColIdx - 1),
                        ):
                            if (
                                    0 <= neighborRow < len(grid)
                                    and 0 <= neighborCol < len(rowArr)
                                    and grid[neighborRow][neighborCol]
                            ):
                                grid[neighborRow][neighborCol] = 0
                                stack.append((neighborRow, neighborCol))
                    maxArea = max(maxArea, curArea)
        return maxArea


print(Solution().maxAreaOfIsland(grid=[[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                       [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                                       [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                                       [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                       [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))
