# to test game interface
from interface import *
def test_parse_input_file():
    assert parse_input_file("test_input_file.txt") == (
        (4,4),[[0, 0], [1, 1], [2, 2], [3, 1]])

# to test returned board interface
def test_format_board():
     ls = [[0,2], [1,2], [2, 0], [2, 1]]
     st = ('..*.','..*.','**..','...*')
     x, y = 4,4
     assert format_board((x,y), ls) == st
