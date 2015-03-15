# to test game interface
from interface import *
def test_parse_input_file():
    assert parse_input_file("test_input_file.txt") == (
        (4,4),[[0, 1], [1, 1], [2, 1]])

# to test returned board interface
def test_format_board():
    ls = [[False, False, False, False],
          [False, True, False, False],
          [False, False, True, False],
          [False, False, False, True]]
    st = "....\n.*..\n..*.\n...*\n"
    assert format_board(ls) == st
