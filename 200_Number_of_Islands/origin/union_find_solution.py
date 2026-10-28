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
    def __init__(self, size: int):  # size = total number of cells in the grid (rows * cols)
        self.parent = list(range(size))  # parent[i] == i means i is a root; at first everyone is their own root (own captain)
        self.rank = [0] * size  # rough tree height, used to keep trees shallow; every tree starts with height 0
        self.count = 0  # number of disjoint sets (islands) currently tracked; starts at 0, numIslands adds 1 per land cell

    def find(self, x: int) -> int:  # return the root (captain) of the set that x belongs to
        # find the root
        root = x  # start walking from x itself
        while self.parent[root] != root:  # a node that does not point to itself is not the root yet
            root = self.parent[root]  # move one step up the chain toward the root
        # path compression: point every node on the way directly at the root
        while self.parent[x] != root:  # walk the same path again, from x up to the root
            self.parent[x], x = root, self.parent[x]  # RHS is evaluated first: x's parent becomes root, then x moves to its OLD parent
        return root  # the captain shared by every node in this set

    def union(self, x: int, y: int) -> bool:  # merge the sets holding x and y; True if they were different sets
        rootX, rootY = self.find(x), self.find(y)  # look up both captains
        if rootX == rootY:  # same captain → x and y are already connected
            return False  # already in the same island

        # union by rank: attach the shorter tree under the taller one
        if self.rank[rootX] < self.rank[rootY]:  # if X's tree is shorter than Y's...
            rootX, rootY = rootY, rootX  # ...swap so rootX is always the taller (or equal) tree
        self.parent[rootY] = rootX  # hang the shorter tree under the taller tree's root
        if self.rank[rootX] == self.rank[rootY]:  # two equally tall trees joined...
            self.rank[rootX] += 1  # ...so the combined tree is one level taller

        self.count -= 1  # two islands became one
        return True  # a real merge happened


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]:  # empty grid, or a grid with empty rows
            return 0  # no cells means no islands

        rows, cols = len(grid), len(grid[0])  # grid dimensions
        uf = UnionFind(rows * cols)  # one slot per cell (water cells get slots too, they are just never used)

        for rowIdx in range(rows):  # scan top to bottom
            for colIdx in range(cols):  # scan left to right inside each row
                if grid[rowIdx][colIdx] != "1":  # water cell
                    continue  # skip it, water never joins any island

                uf.count += 1  # a new land cell is a new island until it gets merged
                cellId = rowIdx * cols + colIdx  # flatten (row, col) into one index

                if rowIdx + 1 < rows and grid[rowIdx + 1][colIdx] == "1":  # a row below exists and that cell is land
                    uf.union(cellId, cellId + cols)  # cell below (one full row ahead in the flat index)
                if colIdx + 1 < cols and grid[rowIdx][colIdx + 1] == "1":  # a column to the right exists and that cell is land
                    uf.union(cellId, cellId + 1)  # cell to the right (next index in the flat array)

        # count may dip below the true value mid-scan (a neighbor can be merged before it is counted),
        # but in the end it equals (land cells) - (successful merges) = number of islands
        return uf.count


if __name__ == "__main__":
    print(Solution().numIslands([["1", "1", "0", "0", "0"],
                                 ["1", "1", "0", "0", "0"],
                                 ["0", "0", "1", "0", "0"],
                                 ["0", "0", "0", "1", "1"]]))  # expected 3