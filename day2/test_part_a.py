import part_a

# assumptions: 
# 	* input is not malformed
# 	* id equals line number

# test decisions:
#	* integration tests only

limits = {
	"red" : 12,
	"blue" : 14,
	"green" : 13,
}

def test_game1():
	line1 = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
	assert part_a.line_has_all_valid_games(limits, line1) == True

def test_game2():
	line1 = "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"
	assert part_a.line_has_all_valid_games(limits, line1) == True

def test_game3():
	line1 = "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
	assert part_a.line_has_all_valid_games(limits, line1) == False

def test_game4():
	line1 = "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"	
	assert part_a.line_has_all_valid_games(limits, line1) == False

def test_game5():
	line1 = "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
	assert part_a.line_has_all_valid_games(limits, line1) == True

def test_correct_answer():
	assert part_a.sum_ids_for_valid_games() == 2716