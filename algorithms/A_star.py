import heapq
import time

from utils import (
    find_start_goal,
    get_neighbors,
    get_cost,
    reconstruct_path,
    calculate_path_cost,
    calculate_path_length
)


def manhattan_distance(current, goal):
    r, c = current
    gr, gc = goal

    return abs(r - gr) + abs(c - gc)


def a_star(grid):

    start_time = time.perf_counter()
    start, goal = find_start_goal(grid)

    # Priority queue:
    # (f_cost, g_cost, node)
    frontier = []

    g_cost = {
        start: 0
    }

    # Parent dictionary for reconstructing the path
    parent = {}

    # Add Start to the priority queue
    h = manhattan_distance(start, goal)
    heapq.heappush(frontier, (h, 0, start))

    nodes_expanded = 0
    max_frontier = 1

    while frontier:

        # Get the node with the smallest f(n)
        f, current_g, current = heapq.heappop(frontier)

        # Ignore outdated entries
        if current_g != g_cost[current]:
            continue

        nodes_expanded += 1

        # Goal reached
        if current == goal:
            break

        # Explore neighbors
        for neighbor in get_neighbors(grid, current):

            # Cost of moving to this neighbor
            move_cost = get_cost(grid[neighbor[0]][neighbor[1]])

            # New cost from Start to neighbor
            tentative_g = current_g + move_cost

            # If this is a cheaper path
            if neighbor not in g_cost or tentative_g < g_cost[neighbor]:

                g_cost[neighbor] = tentative_g
                parent[neighbor] = current

                # Calculate f(n) = g(n) + h(n)
                h = manhattan_distance(neighbor, goal)
                f = tentative_g + h

                heapq.heappush(
                    frontier,
                    (f, tentative_g, neighbor)
                )

        max_frontier = max(max_frontier, len(frontier))

    # Reconstruct path
    path = reconstruct_path(parent, start, goal)

    runtime = time.perf_counter() - start_time

    return {
        "path": path,
        "path_length": calculate_path_length(path),
        "cost": calculate_path_cost(grid, path),
        "nodes_expanded": nodes_expanded,
        "max_frontier": max_frontier,
        "runtime": runtime
    }