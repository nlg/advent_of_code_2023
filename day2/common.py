#!/bin/python

# parser approach - in progress
def parse_line_with_tokens(line):
	limits = {
		"red" : 12,
		"blue" : 14,
		"green" : 13,
	}
	number = ""
	temp = ""
	colon = line.find(':') + 2
	for c in line[colon:]:
		if c == ' ':
			continue
		elif c == ',' or c == ';':
			number = ""
			temp = ""
			continue
		elif c.isnumeric():
			number = number + c			
			continue
		temp = temp + c
		val = limits.get(temp)
		if val != None and val - int(number) < 0:
			return False
	return True


# .[['12', 'blue'], ['15', 'red'], ['2', 'green'], ['17', 'red'], ['8', 'green'], ['5', 'blue'], ['8', 'red'], ['17', 'blue'], ['9', 'green'], ['1', 'blue'], ['4', 'red']]
def game_to_pairs(line):
	number = ""
	temp = ""	
	games = line[line.find(':') + 2:].split(';')
	rv = []
	for game in games:	
		# 12 blue, 15 red, 2 green
		num_space_cubes = game.strip().split(', ')
		# ['12 blue', '15 red', '2 green']
		for num_space_cube in num_space_cubes:
			num_cube_pair = num_space_cube.strip().split(' ')
			rv.append(num_cube_pair)
	return rv