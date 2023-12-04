#!/bin/python

#line = "Game 1: 12 blue, 15 red, 2 green; 17 red, 8 green, 5 blue; 8 red, 17 blue; 9 green, 1 blue, 4 red"

# correct answer 2716


limits = {
		"red" : 12,
		"blue" : 14,
		"green" : 13,
}

def foo(line):
	number = ""
	temp = ""
	colon = line.find(':') + 2
	for c in line[colon:]:
		print(f"c={c}")
		if c == ' ':
			continue
		# reset			
		elif c == ',' or c == ';':
			number = ""
			temp = ""
			continue
		elif c.isnumeric():
			print(f"numeric {number} + {c}")
			number = number + c			
			continue
		temp = temp + c
		val = limits.get(temp)
		print(f"temp={temp} val={val} number={number}")
		if val != None and val - int(number) < 0:
			print("discrd!")
			return False
	return True

def test_foo_one_part():
	line1 = "Game 1: 14 blue,"
	assert foo(line1) == True

def test_foo_two_part():
	line1 = "Game 1: 12 blue, 15 red"
	assert foo(line1) == False

def test_foo_line_bad():
	line1 = "Game 1: 12 blue, 10 red, 11 green; 9 red, 8 green, 5 blue; 8 red, 3 blue; 9 green, 1 blue, 16 red"
	assert foo(line1) == False

def test_foo_line_ok():
	line1 = "Game 1: 12 blue, 10 red, 11 green; 9 red, 8 green, 5 blue; 8 red, 3 blue; 9 green, 1 blue, 10 red"
	assert foo(line1) == True

def pairwise(iterable):
	a = iter(iterable)
	return zip(a,a)

def valid_id(line):
	number = ""
	temp = ""	
	trials = line[line.find(':') + 2:].split(';')
	for trial in trials:	
		part_trial = trial.strip().split(', ')
		for s in part_trial:
			pair = s.strip().split(' ')
			for x,y in pairwise(pair):
				print(f"[{x}][{y}]")
				i = limits.get(y)
				if i != None and int(x) > i:
					return False
	return True





def valid_ids():
	with open("input", "r") as fp:
		running_id = 1
		sum_ids = 0		
		for line in fp.readlines():
			if valid_id(line):
				sum_ids = sum_ids + running_id
			running_id = running_id + 1
	return sum_ids

def running_cubes():
	with open("input", "r") as fp:
		sum = 0		
		for line in fp.readlines():
			
			break

	return sum


sum_ids = valid_ids()
print(f"sum(ids) = {sum_ids}")

# 1. Find the running maximum number of each colored cube
# 2. Must be valid game
# 3. Multiple the number of cubes of each type
# 4. Repeat for each line and summarize the result