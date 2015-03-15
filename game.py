class Board(object):
    def __init__(self, size, live_cells):
        x,y = size
        self.size = size
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
        live = dead = 0
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
                row.append(bool(j))
            ret.append(row)
        return ret

            
def apply_rules(board):
    size = board.size
    live_cells = []
    # 1. A live cell will die if it has less than 2 neighbours
    # 2. A live cell will live on if it has 2 or 3 neighbour
    for ri, row in enumerate(board.cells):
        for ci, column in enumerate(row):
            if board.get(ri, ci) and board.neighbours(ri, ci)[0] in [2,3]: # rule 2
                live_cells.append([ri, ci])
            elif board.get(ri, ci) == False and board.neighbours(ri, ci)[0] == 3: # rule 4
                live_cells.append([ri, ci])
    return Board(size, live_cells)
        
    
    
