import contextlib
import copy
import importlib.util
import io
import os
import random

import pytest

HERE = os.path.dirname(os.path.abspath(__file__))


def load_solution(file_name):
    """
    Load a solution file by path under a unique module name, so it never clashes
    with dfs_recursive_solution.py / dfs_iterative_solution.py of other problems (e.g. 695_Max_Area_of_Island)
    and works no matter which folder PyCharm treats as the source root.
    """
    module_name = f"lc200_{os.path.splitext(file_name)[0]}"
    spec = importlib.util.spec_from_file_location(module_name, os.path.join(HERE, file_name))
    module = importlib.util.module_from_spec(spec)
    # silence anything a solution file prints on import
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


solution0 = load_solution("dfs_recursive_solution.py")
solution1 = load_solution("dfs_iterative_solution.py")
solution2 = load_solution("union_find_solution.py")


def to_grid(rows):
    """Turn ["110", "011"] into [["1", "1", "0"], ["0", "1", "1"]] to keep test cases short."""
    return [list(row) for row in rows]


def reference_num_islands(grid):
    """Simple BFS used as the expected answer for randomized tests."""
    rows, cols = len(grid), len(grid[0])
    seen = set()
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in seen:
                count += 1
                seen.add((r, c))
                queue = [(r, c)]
                while queue:
                    cr, cc = queue.pop()
                    for nr, nc in ((cr + 1, cc), (cr - 1, cc), (cr, cc + 1), (cr, cc - 1)):
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1" and (nr, nc) not in seen:
                            seen.add((nr, nc))
                            queue.append((nr, nc))
    return count


def random_grid(seed):
    rng = random.Random(seed)
    rows, cols = rng.randint(1, 15), rng.randint(1, 15)
    density = rng.random()
    return [["1" if rng.random() < density else "0" for _ in range(cols)] for _ in range(rows)]


# every test below runs once per solution
@pytest.fixture(params=[
    # pytest.param(solution0.Solution, id="solution0-recursive-dfs"),
    # pytest.param(solution1.Solution, id="solution1-iterative-dfs"),
    pytest.param(solution2.Solution, id="solution2-union-find"),
])
def solution(request):
    return request.param()


def num_islands(solution, grid):
    # solutions modify the grid in place, so always pass a copy
    return solution.numIslands(copy.deepcopy(grid))


# (grid, expected)
CASES = [
    # ---------- leetcode examples ----------
    pytest.param(to_grid(["11110", "11010", "11000", "00000"]), 1, id="leetcode_example_1"),
    pytest.param(to_grid(["11000", "11000", "00100", "00011"]), 3, id="leetcode_example_2"),
    # ---------- edge cases ----------
    pytest.param([["1"]], 1, id="single_land_cell"),
    pytest.param([["0"]], 0, id="single_water_cell"),
    pytest.param(to_grid(["000", "000"]), 0, id="all_water"),
    pytest.param(to_grid(["111", "111", "111"]), 1, id="all_land"),
    pytest.param(to_grid(["1101011"]), 3, id="single_row"),
    pytest.param(to_grid(["1", "0", "1", "1", "0", "1"]), 3, id="single_column"),
    # ---------- connectivity ----------
    pytest.param(to_grid(["101", "010", "101"]), 5, id="diagonals_are_not_connected"),
    pytest.param(to_grid(["111", "101", "111"]), 1, id="ring_with_lake_inside"),
    pytest.param(to_grid(["11111", "10001", "10101", "10001", "11111"]), 2, id="island_inside_a_ring"),
    pytest.param(to_grid(["1111", "0001", "1111", "1000", "1111"]), 1, id="snake_shaped_island"),
    pytest.param(to_grid(["101", "101", "111"]), 1, id="u_shape_joined_at_bottom"),
    # ---------- multiple islands ----------
    pytest.param(to_grid(["1001", "0000", "0000", "1001"]), 4, id="islands_in_every_corner"),
    pytest.param(to_grid(["1010", "0101", "1010", "0101"]), 8, id="checkerboard"),
]


@pytest.mark.parametrize("grid, expected", CASES)
def test_fixed_cases(solution, grid, expected):
    assert num_islands(solution, grid) == expected


@pytest.mark.parametrize("seed", range(300))
def test_random_grid_against_reference(solution, seed):
    grid = random_grid(seed)
    assert num_islands(solution, grid) == reference_num_islands(grid)


# ---------- leetcode upper bound: 300 x 300 ----------

def test_max_size_all_land(solution):
    assert num_islands(solution, [["1"] * 300 for _ in range(300)]) == 1


def test_max_size_checkerboard(solution):
    grid = [["1" if (r + c) % 2 == 0 else "0" for c in range(300)] for r in range(300)]
    assert num_islands(solution, grid) == 45000
