import contextlib
import copy
import importlib.util
import io
import os
import random
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))


def load_solution(file_name):
    """
    Load a solution file by path under a unique module name, so it never clashes
    with dfs_recursive_solution.py / dfs_iterative_solution.py of other problems (e.g. 200_Number_of_Islands)
    and works no matter which folder PyCharm treats as the sources root.
    """
    module_name = f"lc695_{os.path.splitext(file_name)[0]}"
    spec = importlib.util.spec_from_file_location(module_name, os.path.join(HERE, file_name))
    module = importlib.util.module_from_spec(spec)
    # the solution files print a sample result on import, silence it
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


solution0 = load_solution("solution0.py")
solution1 = load_solution("solution1.py")


def reference_max_area(grid):
    """Simple BFS used as the expected answer for randomized tests."""
    rows, cols = len(grid), len(grid[0])
    seen = set()
    best = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in seen:
                seen.add((r, c))
                queue = [(r, c)]
                area = 0
                while queue:
                    cr, cc = queue.pop()
                    area += 1
                    for nr, nc in ((cr + 1, cc), (cr - 1, cc), (cr, cc + 1), (cr, cc - 1)):
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and (nr, nc) not in seen:
                            seen.add((nr, nc))
                            queue.append((nr, nc))
                best = max(best, area)
    return best


class MaxAreaOfIslandTests:
    """
    Shared test cases. Not a TestCase itself, so unittest does not run it directly;
    each solution gets its own subclass below.
    """
    solution_cls = None

    def check(self, grid, expected):
        # solutions modify the grid in place, so always pass a copy
        self.assertEqual(self.solution_cls().maxAreaOfIsland(copy.deepcopy(grid)), expected)

    # ---------- leetcode examples ----------

    def test_leetcode_example_1(self):
        grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
        self.check(grid, 6)

    def test_leetcode_example_2_all_water(self):
        self.check([[0, 0, 0, 0, 0, 0, 0, 0]], 0)

    # ---------- edge cases ----------

    def test_empty_grid(self):
        # outside leetcode constraints (m, n >= 1), but should not crash
        self.check([], 0)

    def test_single_land_cell(self):
        self.check([[1]], 1)

    def test_single_water_cell(self):
        self.check([[0]], 0)

    def test_all_land(self):
        self.check([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 9)

    def test_single_row(self):
        self.check([[1, 1, 0, 1, 1, 1, 0, 1]], 3)

    def test_single_column(self):
        self.check([[1], [1], [0], [1], [1], [1], [1]], 4)

    # ---------- connectivity ----------

    def test_diagonals_are_not_connected(self):
        self.check([[1, 0, 1], [0, 1, 0], [1, 0, 1]], 1)

    def test_ring_touching_all_borders(self):
        self.check([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 8)

    def test_snake_shaped_island(self):
        grid = [[1, 1, 1, 1],
                [0, 0, 0, 1],
                [1, 1, 1, 1],
                [1, 0, 0, 0],
                [1, 1, 1, 1]]
        self.check(grid, 14)

    def test_u_shape_joined_at_bottom(self):
        self.check([[1, 0, 1], [1, 0, 1], [1, 1, 1]], 7)

    # ---------- multiple islands ----------

    def test_two_equal_islands(self):
        self.check([[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]], 4)

    def test_largest_island_found_last(self):
        self.check([[1, 0, 0], [0, 0, 1], [0, 1, 1]], 3)

    # ---------- randomized ----------

    def test_random_grids_against_reference(self):
        rng = random.Random(695)
        for i in range(300):
            rows, cols = rng.randint(1, 15), rng.randint(1, 15)
            density = rng.random()
            grid = [[1 if rng.random() < density else 0 for _ in range(cols)] for _ in range(rows)]
            with self.subTest(i=i, rows=rows, cols=cols):
                self.check(grid, reference_max_area(grid))

    # ---------- leetcode upper bound: 50 x 50 ----------

    def test_max_size_all_land(self):
        self.check([[1] * 50 for _ in range(50)], 2500)

    def test_max_size_checkerboard(self):
        self.check([[(r + c) % 2 for c in range(50)] for r in range(50)], 1)


class TestSolution0(MaxAreaOfIslandTests, unittest.TestCase):
    """Recursive DFS"""
    solution_cls = solution0.Solution


class TestSolution1(MaxAreaOfIslandTests, unittest.TestCase):
    """Iterative DFS with a stack"""
    solution_cls = solution1.Solution


if __name__ == "__main__":
    unittest.main(verbosity=2)
