class Board(object):
    def __init__(self, size, live_cells):
        x,y = size
        self.cells = [[0] * y] * x
    
