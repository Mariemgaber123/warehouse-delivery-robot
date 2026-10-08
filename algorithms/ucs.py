import heapq
import time

from utils import (
    get_neighbors,
    get_cost,
    reconstruct_path,
    calculate_path_cost,
    calculate_path_length
)


def uniform_cost_search(grid, start, goal):

    start_time = time.perf_counter()

    frontier = []

    heapq.heappush(frontier, (0, start))

    parent = {
        start: None
    }

    cost_so_far = {
        start: 0
    }

    nodes_expanded = 0
    max_frontier = 1


    while frontier:

        current_cost, current = heapq.heappop(frontier)

        nodes_expanded += 1


        if current == goal:

            path = reconstruct_path(
                parent,
                start,
                goal
            )

            runtime = time.perf_counter() - start_time

            return {
                "path": path,
                "path_length": calculate_path_length(path),
                "cost": calculate_path_cost(grid, path),
                "nodes_expanded": nodes_expanded,
                "max_frontier": max_frontier,
                "runtime": runtime
            }


        for neighbor in get_neighbors(grid, current):

            move_cost = get_cost(
                grid[neighbor[0]][neighbor[1]]
            )

            new_cost = current_cost + move_cost


            if (
                neighbor not in cost_so_far
                or new_cost < cost_so_far[neighbor]
            ):

                cost_so_far[neighbor] = new_cost

                parent[neighbor] = current


                heapq.heappush(
                    frontier,
                    (new_cost, neighbor)
                )


        max_frontier = max(
            max_frontier,
            len(frontier)
        )


    runtime = time.perf_counter() - start_time

    

    return {
        "path": [],
        "path_length": None,
        "cost": None,
        "nodes_expanded": nodes_expanded,
        "max_frontier": max_frontier,
        "runtime": runtime
    }