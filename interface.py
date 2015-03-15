from string import strip, split
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
