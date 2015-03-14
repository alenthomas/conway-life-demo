def test_create_board():
    b = Board((4,4), [])
    assert b.cells == [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
    
