
from utils import (
    find_start_goal,
    display_path
)

from algorithms.A_star import a_star


# Maps

MAP_A = [
    "S..#....",
    "##.#.##.",
    "....~~..",
    ".####.#.",
    "...~..#G"
]

MAP_B = [
    "S~~~~~~~G",
    ".#######.",
    ".........",
    ".#.#.#.#.",
    "........."
]

MAP_C = [
    "S..#....",
    ".#.#.##.",
    "...#..#.",
    ".###.##.",
    "....#..G"
]


MAPS = {
    "MAP A": MAP_A,
    "MAP B": MAP_B,
    "MAP C": MAP_C
}


# Display Map

def print_map(grid):
    for row in grid:
        print(row)


# Main

def main():
    for map_name, grid in MAPS.items():
        print("=" * 40)
        print(map_name)
        print("=" * 40)

        print_map(grid)

        start, goal = find_start_goal(grid)

        print(f"\nStart: {start}")
        print(f"Goal: {goal}")

        result = a_star(grid)

        print("\nA* Results:")
        print(f"Path: {result['path']}")
        print(f"Path length: {result['path_length']}")
        print(f"Cost: {result['cost']}")
        print(f"Nodes expanded: {result['nodes_expanded']}")
        print(f"Max frontier: {result['max_frontier']}")
        print(f"Runtime: {result['runtime']:.6f} seconds")

        print("\nPath on map:")
        display_path(grid, result["path"])


if __name__ == "__main__":
    main()
