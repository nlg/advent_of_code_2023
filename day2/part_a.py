import common

def valid_pair(limits, pair):
	return int(pair[0]) <= limits[pair[1]]  

def line_has_all_valid_games(limits, line):
	pairs = common.game_to_pairs(line)
	for pair in pairs:
		if not valid_pair(limits, pair):
			return False
	return True

def sum_ids_for_valid_games():
	limits = {
		"red" : 12,
		"blue" : 14,
		"green" : 13,
	}	
	with open("input", "r") as fp:
		sum = 0
		for index, line in enumerate(fp.readlines(), 1):
			if line_has_all_valid_games(limits, line):
				sum = sum + index
	return sum