import common

def line_to_max_cubes(line):
	d = {
		"red" : 1,
		"blue" : 1,
		"green" : 1,
	}	
	pairs = common.game_to_pairs(line)
	sum = 0
	for pair in pairs:
		d[pair[1]] = max(int(pair[0]), d[pair[1]])
	return d["red"] * d["blue"] * d["green"]

def sum_max_cubes():
	with open("input", "r") as fp:
		sum = 0		
		for line in fp.readlines():
			sum = sum + line_to_max_cubes(line)
	return sum