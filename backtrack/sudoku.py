DEBUG = False
PROGRESS = False


def print_grid(table):
    for line in table:
        for n in line:
            print("." if n == 0 else n, end="")
        print()


def find_next(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 0:
                return x, y
    return None, None


def check_vertical(grid, x, val):
    for y in range(0, len(grid)):
        if grid[y][x] == val:
            return False
    return True


def check_horizontal(grid, y, val):
    for x in range(0, len(grid[y])):
        if grid[y][x] == val:
            return False
    return True


def solve_one(grid):
    x, y = find_next(grid)
    if DEBUG:
        print("next", x, y)
    # grid = grid.copy()
    if x is None:
        if PROGRESS:
            print("Found:")
            print_grid(grid)
            print()
        return grid

    for val in range(1, 10):
        if DEBUG:
            print("trying", val)
            print()
            print_grid(grid)
            print()
        if check_vertical(grid, x, val) and check_horizontal(grid, y, val):
            grid[y][x] = val
            res = solve_one(grid)
            if res is not False:
                return res
    # Backtracking
    grid[y][x] = 0
    return False


def solve_all(grid, sol):
    x, y = find_next(grid)
    if DEBUG:
        print("next", x, y)
    if x is None:
        if PROGRESS:
            print("Found:")
            print_grid(grid)
            print()
        # Be careful to do a copy to avoid having the last processed
        # grid at the end
        sol.append([l.copy() for l in grid])
        return

    for val in range(1, 10):
        if DEBUG:
            print("trying", val)
            print()
            print_grid(grid)
            print()
        if check_vertical(grid, x, val) and check_horizontal(grid, y, val):
            grid[y][x] = val
            solve_all(grid, sol)
    # Backtracking
    grid[y][x] = 0


def read_grid(data):
    grid = []
    for line in data.split("\n"):
        if line != '':
            grid.append([int(c) if c != '.' else 0 for c in line])
    return grid


if __name__ == "__main__":
    import sys

    data = sys.stdin.read(-1)
    grid = read_grid(data)

    print("Input grid:")
    print()
    print_grid(grid)

    res = solve_one(grid)

    print()
    print("Solution:")
    print()
    print_grid(grid)

# sudoku.py ends here
