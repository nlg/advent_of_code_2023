import common

def test_game_to_pairs():
	line1 = "Game 1: 12 blue, 10 red, 11 green; 9 red, 8 green, 5 blue; 8 red, 3 blue; 9 green, 1 blue, 10 red"
	expected = [['12', 'blue'], ['10', 'red'], ['11', 'green'], ['9', 'red'], ['8', 'green'], ['5', 'blue'], ['8', 'red'], ['3', 'blue'], ['9', 'green'], ['1', 'blue'], ['10', 'red']]
	assert common.game_to_pairs(line1) == expected