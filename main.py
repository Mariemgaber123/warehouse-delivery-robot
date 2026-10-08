from utils import (
    find_start_goal,
    get_neighbors,
    reconstruct_path,
    calculate_path_cost,
    calculate_path_length,
    display_path
)


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


if __name__ == "__main__":
    main()