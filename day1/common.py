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

def filter_numbers(s):
    rv = ""
    for c in s:
        if c.isnumeric():
            rv = rv + c
    return rv

def parse_word(s):
    temp = ""
    for c in s:
        temp = temp + c
        num = words_to_numbers.get(temp)
        if num != None:
            return num

def transform(d, s):
    """
    'xtwone3four' -> '234'
    """
    new_str = ""
    for index, c in enumerate(s):
        if c.isnumeric():
            new_str = new_str + c
            continue
        word_number = parse_word(s[index:])
        if word_number != None:
            new_str = new_str + word_number
    return new_str

def filter_with_transform(line):
    return transform(words_to_numbers, line)

def combine_first_and_last_number(s):
    """ 
    '123' -> 1 + 3 = 4
    """
    if len(s) > 1:
        return int(s[0] + s[-1])
    return int(s[0]+s[0])        


def read_file(parser_func, file_name):
    sum = 0
    with open(file_name, "r") as fp:        
        for line in fp.readlines():
            s = parser_func(line)
            num = combine_first_and_last_number(s)
            sum = sum + num
    return sum    