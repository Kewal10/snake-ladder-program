import unittest

import snake_ladder
from snake_ladder import *

class TestProgram(unittest.TestCase):
    def test_role_dice(self):
        print("test_role_dice: check if 'role_dice()' return values in 1-6 range")
        self.assertTrue(role_dice() in [1,2,3,4,5,6])

        print("\ntest_role_dice: check when 'crooked_dice' is set to True if 'role_dice()' return even values in 1-6 range")
        snake_ladder.crooked_dice = True
        self.assertTrue(role_dice() in [2,4,6])

        print("\ntest_role_dice: check when 'crooked_dice' is set to False if 'role_dice()' return any values in 1-6 range")
        snake_ladder.crooked_dice = False
        self.assertTrue(role_dice() in [1,2,3,4,5,6])

    def test_check_winner(self):
        print("test_check_winner : ")
        self.assertFalse(check_winner('kewal',-1))
        self.assertFalse(check_winner('kewal 1', 101))
        self.assertFalse(check_winner('kewal 1', ''))
        self.assertTrue(check_winner('kewal 2', 100))

if __name__ == '__main__':
    unittest.main()