import sys
from pathlib import Path

# Allow Python to find utils.py in the project root
sys.path.append(str(Path(__file__).resolve().parents[1]))

from utils import (
    find_start_goal,
    get_cost,
    get_neighbors,
    reconstruct_path,
    calculate_path_cost,
    calculate_path_length,
    display_path
)


# Test Map

TEST_MAP = [
    "S..",
    ".#~",
    "..G"
]


# Test find_start_goal

def test_find_start_goal():
    start, goal = find_start_goal(TEST_MAP)

    assert start == (0, 0)
    assert goal == (2, 2)


# Test get_cost

def test_get_cost():
    assert get_cost('.') == 1
    assert get_cost('~') == 3
    assert get_cost('G') == 1


# Test get_neighbors

def test_get_neighbors():
    neighbors = get_neighbors(TEST_MAP, (0, 0))

    assert set(neighbors) == {(1, 0), (0, 1)}


# Test reconstruct_path

def test_reconstruct_path():
    parent = {
        (1, 0): (0, 0),
        (2, 0): (1, 0),
        (2, 1): (2, 0),
        (2, 2): (2, 1)
    }

    path = reconstruct_path(
        parent,
        (0, 0),
        (2, 2)
    )

    assert path == [
        (0, 0),
        (1, 0),
        (2, 0),
        (2, 1),
        (2, 2)
    ]


# Test calculate_path_cost

def test_calculate_path_cost():
    path = [
        (0, 0),
        (0, 1),
        (0, 2),
        (1, 2),
        (2, 2)
    ]

    # . + . + ~ + G
    # 1 + 1 + 3 + 1 = 6
    assert calculate_path_cost(TEST_MAP, path) == 6


# Test calculate_path_length

def test_calculate_path_length():
    path = [
        (0, 0),
        (0, 1),
        (0, 2),
        (1, 2),
        (2, 2)
    ]

    assert calculate_path_length(path) == 4


# Test empty path

def test_empty_path():
    assert calculate_path_cost(TEST_MAP, []) is None
    assert calculate_path_length([]) is None


# Test unreachable goal

def test_reconstruct_empty_path():
    parent = {
        (0, 1): (0, 0)
    }

    path = reconstruct_path(
        parent,
        (0, 0),
        (2, 2)
    )

    assert path == []