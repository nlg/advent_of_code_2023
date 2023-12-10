import pytest
import common

limits = {
    "red": 12,
    "blue": 14,
    "green": 13,
}

testdata = [
    ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", True, 48),
    ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", True, 12),
    (
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        False,
        1560,
    ),
    (
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        False,
        630,
    ),
    ("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", True, 36),
]


@pytest.mark.parametrize("line, verdict, expected", testdata)
def test_string(line, verdict, expected):
    assert common.line_has_all_valid_games(limits, line) == verdict
    assert common.line_to_max_cubes(line) == expected


def test_game_to_pairs():
    line1 = "Game 1: 12 blue, 10 red, 11 green; 9 red, 8 green, 5 blue; 8 red, 3 blue; 9 green, 1 blue, 10 red"
    expected = [
        ["12", "blue"],
        ["10", "red"],
        ["11", "green"],
        ["9", "red"],
        ["8", "green"],
        ["5", "blue"],
        ["8", "red"],
        ["3", "blue"],
        ["9", "green"],
        ["1", "blue"],
        ["10", "red"],
    ]
    assert common.game_to_pairs(line1) == expected


def test_part_a():
    assert common.sum_ids_for_valid_games() == 2716


def test_part_b():
    assert common.sum_max_cubes() == 72227
