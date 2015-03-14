class Board(object):
    def __init__(self, size, live_cells):
        x,y = size
        self.cells = []
        for i in range(x):
            self.cells.append([0] * y)
        for x,y in live_cells:
            self.cells[x][y] = 1

    def get(self, x, y):
        if self.cells[x][y] == 1:
            return True
        else:
            return False
            
    
