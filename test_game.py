from game import Board

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

    
