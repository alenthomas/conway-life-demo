from string import strip, split
from game import *
from sys import argv
from pprint import pprint
# parse input file
def parse_input_file(filename):
    f = open(filename)
    
    size = f.readline()
    size = strip(size)
    x, y = split(size, 'x')
    x = int(x)
    y = int(y)
    string_of_cells = f.readlines()
    cells_new = []
    for line in string_of_cells:
#        cells_new.append(strip(line))
        line = strip(line)
        lines = split(line, ',')
        lines[0] = int(lines[0])
        lines[1] = int(lines[1])
        cells_new.append(lines)
    return (x,y), cells_new

# print board
def format_board(bboard):
    format_text = ""
    for row in bboard:
        for cell in row:
            if cell is True:
                format_text += '*'
            else:
                format_text += '.'
        format_text += '\n'
    return format_text
# takes a keyboard stroke from use
def user_interface():

    x, y = parse_input_file(argv[1])
    #print x
    #print y
    board = Board(x, y)
    nxt_board = apply_rules(board)
    print_board(nxt_board.state())
    #print format_board(nxt_board.state())
    #pprint(vars(board.state))
#    print_board(board.state)
    while True:
        raw_input("")
        print_board(nxt_board.state())

if __name__ == '__main__':
    user_interface()
