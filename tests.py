from main_func import go_hunt, FOUND_MESSAGE, NO_FOUND_MESSAGE
from main_oop import TreasureHunt

import pytest

"""
Treasure Hunt

You need to write a program to explore the above table for a treasure. The values in the table are clues.
Each cell contains a number between 11 and 55, where the ten’s digit represents the row number
and the unit’s digit represents the column number of the cell containing the next clue.

Starting with the upper left corner (at 1,1)
The treasure is a cell whose value is the same as its coordinates.

Example of input						
55 14 25 52 21
44 31 11 53 43
24 13 45 12 34
42 22 43 32 41
51 23 33 54 15 

Example of output						
11 55 15 21 44 32 13 25 43 
"""

# Test data with treasure
DATA_A = """
34 21 32 41 25
14 42 43 14 31
54 45 52 42 23
33 15 51 31 35
21 52 33 13 23
"""
EXPECT_A = ['11', '34', '42', '15', '25', '31', '54', '13', '32', '45', '35', '23',
            '43', '51', '21', '14', '41', '33', '52']

DATA_B = """
55 14 25 52 21
44 31 11 53 43
24 13 45 12 34
42 22 43 32 41
51 23 33 54 15
"""
EXPECT_B = ['11', '55', '15', '21', '44', '32', '13', '25', '43']

# No treasure
DATA_C = """
44 14 25 52 21
55 31 53 11 43
24 13 43 12 34
42 22 45 32 41
51 23 33 15 54
"""
EXPECT_C = ['11', '44', '32', '13', '25', '43', '45', '41', '42', '22', '31', '24']


class TestFunc:
    def test_found(self):
        assert go_hunt(DATA_A) == (EXPECT_A, FOUND_MESSAGE)
        assert go_hunt(DATA_B) == (EXPECT_B, FOUND_MESSAGE)

    def test_no_found(self):
        assert go_hunt(DATA_C) == (EXPECT_C, NO_FOUND_MESSAGE)


class TestCls:
    def test_found(self):
        test_a = TreasureHunt(DATA_A)
        assert test_a.go_hunt() == EXPECT_A
        assert test_a.message == FOUND_MESSAGE

        test_b = TreasureHunt(DATA_B)
        assert test_b.go_hunt() == EXPECT_B
        assert test_b.message == FOUND_MESSAGE

    def test_no_found(self):
        test_c = TreasureHunt(DATA_C)
        assert test_c.go_hunt() == EXPECT_C
        assert test_c.message == NO_FOUND_MESSAGE


if __name__ == "__main__":
    pytest.main(["tests.py"])
    print('ALL TEST COMPLETE')
