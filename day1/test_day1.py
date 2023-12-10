import pytest
import common

testdata1 = [
    ("1abc2", "12", 12),
    ("pqr3stu8vwx", "38", 38),
    ("a1b2c3d4e5f", "2345", 25),
    ("treb7uchet", "7", 7),
]

testdata2 = [
    ("two1nine", "219", 29),
    ("eightwothree", "823", 83),
    ("abcone2threexyz", "123", 13),
    ("xtwone3four", "2134", 24),
    ("4nineeightseven2", "49872", 42),
    ("zoneight234", "18234", 14),
    ("7pqrstsixteen", "76", 76),
    ("1abc2", "12", 12),
    ("pqr3stu8vwx", "38", 38),
    ("a1b2c3d4e5f", "2345", 25),
    ("treb7uchet", "7", 7),
]


@pytest.mark.parametrize("line, exp_str, exp_num", testdata2)
def test_string(line, exp_str, exp_num):
    s = common.filter_with_transform(data)
    assert s == exp_str
    rv = common.combine_first_and_last_number(s)
    assert rv == exp_num


def test_string():
    sum = 0
    for data, exp_str, exp_num in testdata1:
        s = common.filter_with_transform(data)
        rv = common.combine_first_and_last_number(s)
        sum = sum + rv
    assert sum == 142


def test_answer_a():
    sum = common.read_file(common.filter_numbers, "input")
    assert sum == 54605


def test_answer_b():
    num_sum = common.read_file(common.filter_with_transform, "input")
    assert num_sum == 55429
