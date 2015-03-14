from game import Board, apply_rules

def test_create_board():
    b = Board((4,4), [])
    assert b.cells == [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
    b = Board((3,3), [])
    assert b.cells == [[0,0,0], [0,0,0], [0,0,0]]
    b = Board((3,2), [])
    assert b.cells == [[0,0], [0,0], [0,0]]
    b = Board((2,3), [])
    assert b.cells == [[0,0,0], [0,0,0]]

def test_create_nonempty_board():
    b = Board((4,4), [[1,1], [3,0]])
    assert b.cells == [[0,0,0,0], [0,1,0,0], [0,0,0,0], [1,0,0,0]]


def test_get():
    b = Board((4,4), [[1,1]])
    assert b.get(1,1) == True
    assert b.get(0,0) == False


def test_center_neighbours():
    b = Board((4,4), [])
    assert b.neighbours(1,1) == (0, 8)
    b = Board((4,4), [[0,0]])
    assert b.neighbours(1,1) == (1, 7)
    b = Board((4,4), [[1,0], [0,0]])
    assert b.neighbours(1,1) == (2, 6)

    
    
def test_corner_neighbours():
    b = Board((4,4), [])
    assert b.neighbours(3,0) == (0, 3)

def test_edge_neighbours():
    b = Board((4,4), [])
    assert b.neighbours(3,2) == (0, 5)

def test_state():
    b = Board((4,4), [[1,1], [2,2], [3,3]])
    assert b.state() == [[False, False, False, False],
                         [False, True, False, False],
                         [False, False, True, False],
                         [False, False, False, True]]

def test_apply_rules_rule1():
    # 1. A live cell will die if it has less than 2 neighbours
    # O...
    # .O..
    # ....
    # ....
    # Top left corner should die
    b0 = Board((4,4), [[0,0], [1,1]])
    b1 = apply_rules(b0)
    assert b1.get(0,0) is False




    # 2. A live cell will remain alive if it has 2 or 3 neighbours
    # 3. A live cell will die if it has more than 3 neighbours
    # 4. A dead cell will come alive if it has exactly 3 neighbours
    
