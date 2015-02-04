def get_neighbors(m, n, i, j):
    """Given the dimensions of the grid (m rings, n cells), returns a
    list containing the rings and cells of the neighbors."""
    neighbors = []
    neighbors.extend(
        [[i, (j - 1 + n) % n],
         [i, (j + 1) % n]])
    
    if i == 0:
        neighbors.extend(
            [[i, (j + n / 2 - 1) % n],
             [i, (j + n / 2) % n],
             [i, (j + n / 2 + 1) % n]])
    else:
        neighbors.extend(
            [[i - 1, (j - 1 + n) % n],
             [i - 1, j],
             [i - 1, (j + 1) % n]])
        
    if i == (m - 1):
        neighbors.extend(
            [[i, (j + n / 2 - 1) % n],
             [i, (j + n / 2) % n],
             [i, (j + n / 2 + 1) % n]])
    else:
        neighbors.extend(
            [[i + 1, (j - 1 + n) % n],
             [i + 1, j],
             [i + 1, (j + 1) % n]])
    return neighbors

def dims(grid):
    """Returns a tuple containing the dimensions of the grid."""
    return (len(grid), len(grid[0]))

def will_be_live(grid, live_neighbor_counts, i, j):
    live_neighbor_count = live_neighbor_counts[i][j]
    return ((grid[i][j] and (2 <= live_neighbor_count <= 3)) or
            (not grid[i][j] and live_neighbor_count == 3))

def get_live_neighbor_counts(grid):
    m, n = dims(grid)

    live_neighbor_counts = [[0 for j in range(n)] for i in range(m)]
    
    for i in range(m):
        for j in range(n):
            if grid[i][j]:
                for neighbor in get_neighbors(m, n, i, j):
                    live_neighbor_counts[neighbor[0]][neighbor[1]] += 1

    return live_neighbor_counts
                    
def get_next_generation(grid):
    m, n = dims(grid)
    live_neighbor_counts = get_live_neighbor_counts(grid)
    return [[will_be_live(grid, live_neighbor_counts, i, j) for j in range(n)] for i in range(m)]
    
def solve(grid, generations):
    m, n = dims(grid)
    
    for i in range(generations):
        grid = get_next_generation(grid)

    live_cells = []
    for i in range(m):
        for j in range(n):
            if grid[i][j]: live_cells.append([i, j])
            
    return live_cells

def main():
    case = 1
    while True:
        m, n = map(int, raw_input().split())

        if m == n == 0:
            break

        
        live_cells_count = int(raw_input())

        live_cells_unpaired = []
        while len(live_cells_unpaired) < (live_cells_count * 2):
            live_cells_unpaired.extend(map(int, raw_input().split()))

        live_cells = [live_cells_unpaired[i:i+2] for i in range(0, len(live_cells_unpaired), 2)]
        generations = int(raw_input())

        # In form grid[ring][cell]
        grid = [[([i, j] in live_cells) for j in range(n)] for i in range(m)]
        
        live_cells = solve(grid, generations)

        if len(live_cells) == 0:
            print "Case %d: %d %d %d %d %d" % (case, 0, -1, -1, -1, -1)
        else:
            print "Case %d: %d %d %d %d %d" % (
                case,
                len(live_cells),
                live_cells[0][0],
                live_cells[0][1],
                live_cells[-1][0],
                live_cells[-1][1])
                
        case += 1
        
if __name__ == "__main__":
    main()
