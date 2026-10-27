"""
Union Find solution for 200_Number_of_Islands.

Idea:
    - Every land cell starts as its own island (its own set)
    - For each land cell, union it with the land cell to its right and below
      (up and left were already handled when we visited those cells)
    - Every successful union merges two islands into one, so the count drops by 1

Time Complexity: O(m * n * α(m * n)) ≈ O(m * n), α is the inverse Ackermann function
Space Complexity: O(m * n) for the parent / rank arrays
"""


class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size))  # parent[i] == i means i is a root
        self.rank = [0] * size  # rough tree height, used to keep trees shallow
        self.count = 0  # number of disjoint sets (islands) currently tracked

    def find(self, x: int) -> int:
        # find the root
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        # path compression: point every node on the way directly at the root
        while self.parent[x] != root:
            self.parent[x], x = root, self.parent[x]
        return root

    def union(self, x: int, y: int) -> bool:
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY:
            return False  # already in the same island

        # union by rank: attach the shorter tree under the taller one
        if self.rank[rootX] < self.rank[rootY]:
            rootX, rootY = rootY, rootX
        self.parent[rootY] = rootX
        if self.rank[rootX] == self.rank[rootY]:
            self.rank[rootX] += 1

        self.count -= 1  # two islands became one
        return True


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        uf = UnionFind(rows * cols)

        for rowIdx in range(rows):
            for colIdx in range(cols):
                if grid[rowIdx][colIdx] != "1":
                    continue

                uf.count += 1  # a new land cell is a new island until it gets merged
                cellId = rowIdx * cols + colIdx  # flatten (row, col) into one index

                if rowIdx + 1 < rows and grid[rowIdx + 1][colIdx] == "1":
                    uf.union(cellId, cellId + cols)  # cell below
                if colIdx + 1 < cols and grid[rowIdx][colIdx + 1] == "1":
                    uf.union(cellId, cellId + 1)  # cell to the right

        return uf.count


if __name__ == "__main__":
    print(Solution().numIslands([["1", "1", "0", "0", "0"],
                                 ["1", "1", "0", "0", "0"],
                                 ["0", "0", "1", "0", "0"],
                                 ["0", "0", "0", "1", "1"]]))  # expected 3
