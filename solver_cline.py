import numpy as np
import example_puzzles
from copy import deepcopy

sudoku = np.array(example_puzzles.easy)

def get_subgrids(grid):
        subgrids = []
        for box_i in range(3):
            for box_j in range(3):
                subgrid = []
                for i in range(3):
                    for j in range(3):
                        subgrid.append(grid[3*box_i + i][3*box_j + j])
                subgrids.append(subgrid)
        return subgrids

def fill_cand(grid):
    def subgrid_index(i, j):
        return (i//3) * 3 + j // 3
    box = get_subgrids(grid)

    def get_cands(grid, i, j):
        rowtchck = set(grid[i])
        coltchck = set(grid[:, j])
        subtchck = set(box[subgrid_index(i, j)])

        common = rowtchck | coltchck | subtchck
        cands = set(range(1,10)) - common
        return list(cands)

    candidates = []
    for i in range(9):
        row_cands = []
        for j in range(9):
            if not grid[i][j]:
                row_cands.append(get_cands(grid, i, j))
            else:
                row_cands.append([grid[i][j]])
        candidates.append(row_cands)
    return candidates

def filter_candidates(grid):
    test_grid = grid.copy()
    candidates = fill_cand(grid)
    filtered_candidates = deepcopy(candidates)
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for candidate in candidates[i][j]:
                    test_grid[i][j] = candidate
                    if not is_validguess(fill_sing(test_grid)):
                        filtered_candidates[i][j].remove(candidate)
                    test_grid[i][j] = 0
    return filtered_candidates

def fill_sing(grid, candidates = None):
    grid = grid.copy()
    if not candidates:
        candidates = fill_cand(grid)
    keep_fill = True
    while keep_fill:
        keep_fill = False
        for i in range(9):
            for j in range(9):
                if len(candidates[i][j]) == 1 and grid[i][j] == 0 :
                    grid[i][j] = candidates[i][j][0]
                    candidates = merge(fill_cand(grid), candidates)
                    keep_fill = True
    return grid

def merge(candidates_1, candidates_2):
    candidates_min = []
    for i in range(9):
        row = []
        for j in range(9):
            if len(candidates_1[i][j]) < len(candidates_2[i][j]):
                row.append(candidates_1[i][j][:])
            else:
                row.append(candidates_2[i][j][:])
        candidates_min.append(row)
    return candidates_min

def is_solution(grid):
    sol = False
    box = get_subgrids(grid)

    if np.all(np.sum(grid, axis=1) == 45 ) and \
        np.all(np.sum(grid, axis=0) == 45 ) and \
            np.all(np.sum(box, axis=1) == 45 ):
            sol = True
    return sol

def is_validguess(grid):
    candidates = fill_cand(grid)
    for i in range(9):
        for j in range(9):
            if len(candidates[i][j]) == 0:
                return False
    return True

def guessing(grid, candidates = None):
    grid = grid.copy()
    if not candidates:
        candidates = fill_cand(grid)
    min_len = sorted(list(set(map(len, np.array(candidates, dtype=object).reshape(1,81)[0]))))[1]

    for i in range(9):
        for j in range(9):
            if len(candidates[i][j]) == min_len:
                for guess in candidates[i][j]:
                    grid[i][j] = guess
                    solution = filtered_solve(grid)
                    if solution is not None:
                        return solution
                    grid[i][j] = 0

tries = 0

def filtered_solve(grid):
    global tries
    tries+=1
    candidates = filter_candidates(grid)
    grid = fill_sing(grid, candidates)
    if is_solution(grid):
        return grid
    if not is_validguess(grid):
        return None
    return guessing(grid, candidates)

gridsss = filtered_solve(sudoku)

for i in gridsss:
    print(i)
print(is_solution(gridsss))
print(tries)