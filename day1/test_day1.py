#!/bin/python3

words_to_numbers = {
    'one' : '1',
    'two' : '2',    
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
    'eight' : '8',
    'nine' : '9',
}

def foo(str1):
    """ 'two1nine' -> '219' """
    new_str = ""
    index = 0
    for c in str1:
        # Either it's an actual number
        if c.isnumeric():
            new_str = new_str + c
            #print(f"found string ={new_str}")
            index = index + 1
            continue
        # Or we're dealing with a char, in which case we will 
        # do a sliding window of increasing size
        temp = ""
        for c2 in str1[index:]:    
            # have we built a convertable string?
            temp = temp + c2            
            num = words_to_numbers.get(temp)
            #print(f"temp={temp} num={num}")
            # yup, add it and break the inner loop
            if num != None:
                new_str = new_str + num
                break
            # no, continue munching until the end
        index = index + 1    
    return new_str

def test_num():
    rv = foo("1")
    assert rv == "1"

def test_str():
    rv = foo("one")
    assert rv == "1" 

def test_combined():
    rv = foo("1one")
    assert rv == "11"

def test_combined_reverse():
    rv = foo("one1")
    assert rv == "11"

def test_multi_num():
    rv = foo("21")
    assert rv == "21"

def test_multi_str():
    rv = foo("onethreefour9")
    assert rv == "1349"


def read_numbers():
    with open("input", "r") as fp:
        l=[]
        for line in fp.readlines():
            new_line = ""            
            l.append(foo(line))
        return l

def parse_lines(ll):
    number = 0
    rounds = 0
    rounds_to_complete = None
    skip = 0
    for l in ll:
        if skip > 0:
            skip = skip - 1
            continue
        elif len(l) == 1:
            print(f"{number} + {l[0]} = {number+int(l[0])} + {int(l[0])}")
            number = number + int(l[0]+l[0])
        elif len(l) > 1:
            print(f"{number} + {l[0]} + {l[-1]} = {number + int(l[0] + l[1])}")
            number = number + int(l[0] + l[-1])
        rounds = rounds + 1
        if rounds == rounds_to_complete and rounds_to_complete != None:
            break
    return number

ll = read_numbers()
num = parse_lines(ll)
print(f"final number = {num}")