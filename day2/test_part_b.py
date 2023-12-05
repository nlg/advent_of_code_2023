import part_b

def test_game1():
	line = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
	assert part_b.line_to_max_cubes(line) == 48

def test_game2():
	line = "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"
	assert part_b.line_to_max_cubes(line) == 12

def test_game3():
	line = "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
	assert part_b.line_to_max_cubes(line) == 1560

def test_game4():
	line = "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"
	assert part_b.line_to_max_cubes(line) == 630

def test_game5():
	line = "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
	assert part_b.line_to_max_cubes(line) == 36

def test_correct_answer():
	assert part_b.sum_max_cubes() == 72227