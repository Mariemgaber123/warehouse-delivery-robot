# Movement Directions

DIRECTIONS = [
    (-1, 0),  # Up
    (1, 0),   # Down
    (0, -1),  # Left
    (0, 1)    # Right
]


# Find Start and Goal

def find_start_goal(grid):
    start = None
    goal = None

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == 'S':
                start = (r, c)
            elif grid[r][c] == 'G':
                goal = (r, c)

    return start, goal


# Get Movement Cost

def get_cost(cell):
    if cell == '~':
        return 3

    return 1


# Get Valid Neighbors

def get_neighbors(grid, current):
    r, c = current
    neighbors = []

    for dr, dc in DIRECTIONS:
        nr = r + dr
        nc = c + dc

        # Check that the new position is inside the grid
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):

            # Ignore walls
            if grid[nr][nc] != '#':
                neighbors.append((nr, nc))

    return neighbors


# Reconstruct Path

def reconstruct_path(parent, start, goal):
    if goal not in parent:
        return []

    path = []
    current = goal

    while current != start:
        path.append(current)
        current = parent[current]

    path.append(start)

    # Reverse to get Start -> Goal
    path.reverse()

    return path


# Calculate Path Cost

def calculate_path_cost(grid, path):
    if not path:
        return None

    cost = 0

    # Start is not counted
    for r, c in path[1:]:
        cost += get_cost(grid[r][c])

    return cost


# Calculate Path Length

def calculate_path_length(path):
    if not path:
        return None

    # Number of moves
    return len(path) - 1


# Display Path

def display_path(grid, path):
    display_grid = [list(row) for row in grid]

    for r, c in path:

        # Keep S and G unchanged
        if display_grid[r][c] not in ('S', 'G'):
            display_grid[r][c] = '*'

    for row in display_grid:
        print(''.join(row))