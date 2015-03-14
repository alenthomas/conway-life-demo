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
            
    def neighbours(self, x, y):
        live = 0
        dead = 0
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if i == x and j == y:
                    continue
                if i < 0 or j < 0:
                    continue
                try:
                    if self.cells[i][j] == 1:
                        live += 1
                    if self.cells[i][j] == 0:
                        dead += 1
                except IndexError:
                    pass
        return (live, dead)
    

    def state(self):
        ret = []
        for i in self.cells:
            row = []
            for j in i:
                if j == 1:
                    row.append(True)
                else:
                    row.append(False)
            ret.append(row)
        return ret
            
