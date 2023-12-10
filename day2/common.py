# .[['12', 'blue'], ['15', 'red'], ['2', 'green'], ['17', 'red'], ['8', 'green'], ['5', 'blue'], ['8', 'red'], ['17', 'blue'], ['9', 'green'], ['1', 'blue'], ['4', 'red']]
def game_to_pairs(line):
    number = ""
    temp = ""
    games = line[line.find(":") + 2 :].split(";")
    rv = []
    for game in games:
        # 12 blue, 15 red, 2 green
        num_space_cubes = game.strip().split(", ")
        # ['12 blue', '15 red', '2 green']
        for num_space_cube in num_space_cubes:
            num_cube_pair = num_space_cube.strip().split(" ")
            rv.append(num_cube_pair)
    return rv


def valid_pair(limits, pair):
    return int(pair[0]) <= limits[pair[1]]


def line_has_all_valid_games(limits, line):
    pairs = game_to_pairs(line)
    for pair in pairs:
        if not valid_pair(limits, pair):
            return False
    return True


def line_to_max_cubes(line):
    d = {
        "red": 1,
        "blue": 1,
        "green": 1,
    }
    pairs = game_to_pairs(line)
    sum = 0
    for pair in pairs:
        d[pair[1]] = max(int(pair[0]), d[pair[1]])
    return d["red"] * d["blue"] * d["green"]


def sum_ids_for_valid_games():
    limits = {
        "red": 12,
        "blue": 14,
        "green": 13,
    }
    with open("input", "r") as fp:
        sum = 0
        for index, line in enumerate(fp.readlines(), 1):
            if line_has_all_valid_games(limits, line):
                sum = sum + index
    return sum


def sum_max_cubes():
    with open("input", "r") as fp:
        sum = 0
        for line in fp.readlines():
            sum = sum + line_to_max_cubes(line)
    return sum
