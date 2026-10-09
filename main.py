import pandas as pd

from utils import find_start_goal, display_path
from algorithms.A_star import a_star
from algorithms.ucs import uniform_cost_search


# =========================
# Maps
# =========================

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


# =========================
# Display Map
# =========================

def print_map(grid):
    for row in grid:
        print(row)


# =========================
# Main
# =========================

def main():
    results = []

    for map_name, grid in MAPS.items():
        print("=" * 40)
        print(map_name)
        print("=" * 40)

        print_map(grid)

        start, goal = find_start_goal(grid)

        print(f"\nStart: {start}")
        print(f"Goal: {goal}")

        # Run UCS
        ucs_result = uniform_cost_search(grid, start, goal)

        print("\nUCS Results:")
        print(f"Path: {ucs_result['path']}")
        print(f"Path length: {ucs_result['path_length']}")
        print(f"Cost: {ucs_result['cost']}")
        print(f"Nodes expanded: {ucs_result['nodes_expanded']}")
        print(f"Max frontier: {ucs_result['max_frontier']}")
        print(f"Runtime: {ucs_result['runtime']:.6f} seconds")

        if ucs_result["path"]:
            print("\nUCS Path on map:")
            display_path(grid, ucs_result["path"])
        else:
            print("No path found")

        results.append({
            "Map": map_name,
            "Algorithm": "UCS",
            "Path Length": ucs_result["path_length"],
            "Cost": ucs_result["cost"],
            "Nodes Expanded": ucs_result["nodes_expanded"],
            "Max Frontier": ucs_result["max_frontier"],
            "Runtime": ucs_result["runtime"]
        })

        # Run A*
        a_result = a_star(grid)

        print("\nA* Results:")
        print(f"Path: {a_result['path']}")
        print(f"Path length: {a_result['path_length']}")
        print(f"Cost: {a_result['cost']}")
        print(f"Nodes expanded: {a_result['nodes_expanded']}")
        print(f"Max frontier: {a_result['max_frontier']}")
        print(f"Runtime: {a_result['runtime']:.6f} seconds")

        if a_result["path"]:
            print("\nA* Path on map:")
            display_path(grid, a_result["path"])
        else:
            print("No path found")

        results.append({
            "Map": map_name,
            "Algorithm": "A*",
            "Path Length": a_result["path_length"],
            "Cost": a_result["cost"],
            "Nodes Expanded": a_result["nodes_expanded"],
            "Max Frontier": a_result["max_frontier"],
            "Runtime": a_result["runtime"]
        })

    # Print the complete results table once
    print("\n" + "=" * 60)
    print("FINAL RESULTS TABLE")
    print("=" * 60)

    df = pd.DataFrame(results)
    print(df.to_string(index=False))


if __name__ == "__main__":
    main()