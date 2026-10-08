Warehouse Delivery Robot – Search Algorithms
Project Overview

This project implements search algorithms to find a path for a warehouse delivery robot from a starting position S to a goal position G on a grid.

The robot can move in four directions:

Up
Down
Left
Right

The project uses weighted movement costs, so finding the shortest path does not always mean finding the cheapest path.

Problem Description

The warehouse is represented as a grid:

Symbol	Meaning	Movement Cost
S	Start position	0
G	Goal position	1
.	Normal floor	1
~	Expensive floor	3
#	Wall	Cannot enter

The cost of the starting cell S is not included in the total path cost.

The objective is to find a path from S to G while minimizing the total movement cost.

Algorithms

The project uses two search algorithms:


## A* Search Algorithm

### Overview

A* is an informed search algorithm used to find a path from the start position `S` to the goal position `G`.

It is suitable for this warehouse problem because the grid contains different movement costs.

### Evaluation Function

A* selects nodes using:

```text
f(n) = g(n) + h(n)
```

where:

* `g(n)` is the actual cost from the start node to the current node.
* `h(n)` is the estimated cost from the current node to the goal.
* `f(n)` is the estimated total cost of reaching the goal through the current node.

### Heuristic

The Manhattan distance is used as the heuristic:

```text
h(n) = |row - goal_row| + |column - goal_column|
```

It is appropriate because the robot can only move in four directions: up, down, left, and right.

### Movement Costs

The algorithm accounts for the different cell costs:

* `.` → cost `1`
* `~` → cost `3`
* `G` → cost `1`
* `#` → blocked

The cost of the starting cell `S` is not counted.

### Implementation

The A* implementation is located in:

```text
algorithms/A_star.py
```

The algorithm uses a priority queue to select the node with the smallest `f(n)` value.

It also keeps track of:

* `g_cost` for the cheapest known cost to each node.
* `parent` for reconstructing the final path.
* `nodes_expanded` for the number of expanded nodes.
* `max_frontier` for the maximum priority queue size.
* `runtime` for execution time.

### A* Results

The current implementation was tested on all three provided maps.

| Map   | Path Length | Cost | Nodes Expanded | Max Frontier | Result     |
| ----- | ----------: | ---: | -------------: | -----------: | ---------- |
| MAP A |          11 |   15 |             21 |            5 | Path found |
| MAP B |          12 |   12 |             15 |            7 | Path found |
| MAP C |           — |    — |             13 |            3 | No path    |

### MAP A Path

```text
S**#....
##*#.##.
..******
.####.#*
...~..#G
```

### MAP B Path

```text
S~~~~~~~G
*#######*
*********
.#.#.#.#.
.........
```

MAP B demonstrates that A* considers movement cost rather than simply choosing the path with the fewest moves. The selected path is longer in number of moves but has a lower total cost.

### MAP C

No valid path exists from `S` to `G`, and the algorithm correctly reports that no path was found.
