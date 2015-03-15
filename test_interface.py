# to test game interface
from interface import parse_input_file
def test_parse_input_file():
    assert parse_input_file("test_input_file.txt") == (
        (4,4),[[0, 0], [1, 1], [2, 2], [3, 1]])
