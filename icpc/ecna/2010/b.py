def flip_left(grid):
    """Flips the first column onto the second column."""
    tmp_grid = []
    for row in grid:
        tmp_row = row
        tmp_row[0] = map(lambda x: -x, reversed(tmp_row[0]))
        tmp_row[1].extend(tmp_row[0])
        tmp_grid.append(tmp_row[1:])

    return tmp_grid

def flip_right(grid):
    """Flips the last column onto the second-from-last column."""
    n = len(grid[0])

    tmp_grid = []
    for row in grid:
        tmp_row = row
        tmp_row[n - 1] = map(lambda x: -x, reversed(tmp_row[n - 1]))
        tmp_row[n - 2].extend(tmp_row[n - 1])
        tmp_grid.append(tmp_row[:n - 1])

    return tmp_grid

def flip_top(grid):
    """Flips the top row onto the second row."""
    n = len(grid[0])

    tmp_grid = grid

    for i in range(n):
        flipped = map(lambda x: -x, reversed(tmp_grid[0][i]))
        tmp_grid[1][i].extend(flipped)

    return tmp_grid[1:]

def flip_bottom(grid):
    """Flips the last row onto the second-from-last row."""
    m = len(grid)
    n = len(grid[0])

    tmp_grid = grid

    for i in range(n):
        flipped = map(lambda x: -x, reversed(tmp_grid[m - 1][i]))
        tmp_grid[m - 2][i].extend(flipped)

    return tmp_grid[:m - 1]

def solve(grid, flips):
    """Accepts an m by n grid of cards (integers) and a list of characters
    representing the flips to be performed on those cards. Returns a list of
    integers representing the deck after that series of flips has been
    performed."""

    # Each card slot needs to be a list, because there could be multiple cards
    # in a single slot.

    # grid[0][0][1] is on top of grid[0][0][0]
    tmp_grid = []
    for row in grid:
        tmp_grid.append(map(lambda x: [x], row))
    grid = tmp_grid


    for flip in flips:
        if flip == "L":
            grid = flip_left(grid)
        elif flip == "R":
            grid = flip_right(grid)
        elif flip == "T":
            grid = flip_top(grid)
        elif flip == "B":
            grid = flip_bottom(grid)

    return grid[0][0]


def main():
    case = 1
    while True:
        dims = raw_input()
        if not dims:
            continue

        n, m = map(int, dims.split())

        if (n == 0 and m == 0):
            break

        grid = []
        for i in range(n):
            grid.append(map(int, raw_input().split()))

        # Avoid the case where there are no flips because the grid is 1x1
        flips = []
        if ((n + m - 2) > 0):
            flips = list(raw_input())

        solution = filter(lambda x: x > 0, solve(grid, flips))
        solution_str = "".join(map(lambda x: " %d" % (x), solution))

        print "Case %d:%s" % (case, solution_str)
        case += 1

if __name__ == "__main__":
    main()
