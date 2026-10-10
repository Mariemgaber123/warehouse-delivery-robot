
from collections import deque
import time

from utils import (
    get_neighbors,
    reconstruct_path,
    calculate_path_cost,
    calculate_path_length
)


def bfs(grid, start, goal):

    start_time = time.perf_counter()

    frontier = deque([start])

    parent = {
        start: None
    }

    visited = {
        start
    }

    nodes_expanded = 0
    max_frontier = 1

    while frontier:

        current = frontier.popleft()

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

            if neighbor not in visited:

                visited.add(neighbor)

                parent[neighbor] = current

                frontier.append(neighbor)

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
