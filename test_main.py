import unittest
from main import TicTacToe 

class Test_TicTacToe(unittest.TestCase):


    # 1. Checking the "equals" function
    def test_equals_func(self):
        t = TicTacToe([' ']) # Stub 
        self.assertTrue(t.equals(['X', 'X', 'X', 'X']))
        self.assertTrue(t.equals(['O', 'O', 'O', 'O']))

        self.assertFalse(t.equals(['X', 'X', ' ', 'X']))
        self.assertFalse(t.equals(['X', 'X', 'O', 'O']))
        


    # 2. Checking the "get_winner" function

        # 2.1 Checking when field sizes <= 5

    def test_main_diagonal_is_winner_size3(self):
        board = [['X', 'O', 'O'],
                 ['O', 'X', 'X'],
                 [' ', ' ', 'X']]
        t = TicTacToe(board)
        self.assertEqual(t.get_winner(), 'X')

    def test_secondary_diagonal_is_winner_size4(self):
        board = [['O', ' ', ' ', 'X'],
                 ['O', 'O', 'X', ' '],
                 [' ', 'X', ' ', ' '],
                 ['X', ' ', ' ', ' ']]
        t = TicTacToe(board)
        self.assertEqual(t.get_winner(), 'X')

    def test_second_column_is_winner_size4(self):
        board = [['O', 'O', ' ', 'X'],
                 ['X', 'O', 'O', 'X'],
                 ['X', 'O', 'X', 'X'],
                 ['X', 'O', ' ', 'O']]
        t = TicTacToe(board)
        self.assertEqual(t.get_winner(), 'O')

    def test_third_row_is_winner_size5(self):
        board = [['O', 'X', 'X', 'X', ' '],
                 ['X', 'X', 'O', 'X', 'X'],
                 ['O', 'O', 'O', 'O', 'O'],
                 ['X', 'O', 'X', 'O', ' ']]
        t = TicTacToe(board)
        self.assertEqual(t.get_winner(), 'O')


        # 2.1 Checking when field sizes > 5

    def test_first_column_is_winner_size7(self):
        board = [['X', 'X', 'X', 'X', 'O', ' ', ' '],
                 ['X', ' ', ' ', 'X', ' ', ' ', ' '],
                 ['O', ' ', ' ', 'X', ' ', ' ', ' '],
                 ['O', ' ', ' ', ' ', ' ', ' ', ' '],
                 ['O', ' ', ' ', 'O', ' ', ' ', ' '],
                 ['O', ' ', ' ', ' ', ' ', ' ', ' '],
                 ['O', ' ', ' ', ' ', ' ', ' ', ' '],]
        t = TicTacToe(board)
        self.assertEqual(t.get_winner(), 'O')

    def test_second_row_is_winner_size7(self):
        board = [['X', 'X', 'X', 'X', 'O', 'O', ' '],
                 ['O', 'X', 'X', 'X', 'X', 'X', 'O'],
                 ['O', ' ', ' ', 'X', ' ', 'O', ' '],
                 ['X', ' ', 'X', ' ', ' ', 'O', ' '],
                 ['O', 'X', ' ', 'O', ' ', ' ', ' '],
                 ['X', 'O', 'O', 'O', ' ', ' ', ' '],
                 ['O', ' ', ' ', 'O', ' ', ' ', ' '],]
        t = TicTacToe(board)
        self.assertEqual(t.get_winner(), 'X')

    def test_secondary_diagonal_is_winner_size7(self):
        board = [['X', 'X', 'X', 'X', 'O', 'O', ' '],
                 ['O', ' ', ' ', 'X', 'X', ' ', ' '],
                 ['O', ' ', ' ', 'X', ' ', ' ', ' '],
                 ['X', ' ', 'X', ' ', ' ', ' ', ' '],
                 ['O', 'X', ' ', 'O', ' ', ' ', ' '],
                 ['X', 'O', 'O', 'O', ' ', ' ', ' '],
                 ['O', ' ', ' ', 'O', ' ', ' ', ' '],]
        t = TicTacToe(board)
        self.assertEqual(t.get_winner(), 'X')

    def test_main_diagonal_is_winner_size7(self):
        board = [['X', 'X', 'X', 'X', 'O', ' ', ' '],
                 ['O', ' ', ' ', 'X', 'X', ' ', ' '],
                 ['O', 'O', ' ', 'X', ' ', ' ', ' '],
                 ['O', 'X', 'O', 'X', 'X', 'X', ' '],
                 ['O', 'O', ' ', 'O', ' ', ' ', ' '],
                 ['X', 'O', 'O', 'O', 'O', ' ', ' '],
                 ['O', ' ', ' ', 'O', 'X', ' ', ' '],]
        t = TicTacToe(board)
        self.assertEqual(t.get_winner(), 'O')

    def test_tie_size7(self): # No free cells, no winners -> tie
        board = [['X', 'X', 'X', 'X', 'O', 'O', 'X'],
                 ['O', 'X', 'X', 'X', 'X', 'O', 'O'],
                 ['O', 'O', 'O', 'X', 'O', 'O', 'X'],
                 ['O', 'X', 'O', 'X', 'O', 'X', 'O'],
                 ['O', 'O', 'X', 'O', 'X', 'X', 'X'],
                 ['X', 'O', 'X', 'O', 'X', 'O', 'X'],
                 ['O', 'O', 'X', 'O', 'X', 'O', 'X'],]
        t = TicTacToe(board)
        self.assertEqual(t.get_winner(), "tie")

    def test_NULL_size7(self): # There are no winners, the game continues
        board = [['X', 'X', 'X', 'X', 'O', ' ', ' '],
                 ['O', ' ', ' ', 'X', 'X', ' ', ' '],
                 ['O', 'O', ' ', 'X', ' ', ' ', ' '],
                 ['O', 'X', 'O', 'X', 'X', 'X', ' '],
                 ['O', 'O', ' ', 'O', ' ', ' ', ' '],
                 ['X', 'O', 'O', 'O', 'X', ' ', ' '],
                 ['O', ' ', ' ', 'O', 'X', 'O', ' '],]
        t = TicTacToe(board)
        self.assertEqual(t.get_winner(), None)



    # 3. Checking the best move

    def test_get_best_move_1_size4(self):
        board = [['O', ' ', ' ', 'X'],
                 ['O', 'O', 'X', ' '],
                 [' ', 'X', ' ', ' '],
                 [' ', ' ', ' ', ' ']]
        t = TicTacToe(board)
        self.assertEqual(t.get_best_move(), [3, 0])

    def test_get_best_move_2_size4(self):
        board = [['O', 'X', ' ', 'X'],
                 ['O', 'O', 'O', ' '],
                 ['X', 'X', 'X', ' '],
                 ['O', ' ', ' ', ' ']]
        t = TicTacToe(board)
        self.assertEqual(t.get_best_move(), [2, 3])

    def test_get_best_move_3_size4(self):
        board = [['O', 'X', ' ', 'X'],
                 ['O', 'O', 'O', ' '],
                 ['X', 'X', ' ', ' '],
                 ['O', ' ', 'X', ' ']]
        t = TicTacToe(board)
        self.assertEqual(t.get_best_move(), [1, 3])

    def test_get_best_move_4_size5(self):
        board = [['O', 'X', 'X', 'X', ' '],
                 ['O', 'X', 'X', 'O', 'O'],
                 ['X', 'X', 'O', 'X', 'O'],
                 ['O', 'O', 'O', 'X', 'O'],
                 ['O', 'X', ' ', 'X', ' '],]
        t = TicTacToe(board)
        self.assertEqual(t.get_best_move(), [0, 4])

    def test_get_best_move5_size7(self):
        board = [['O', 'O', 'O', 'O', 'X', 'O', 'X'],
                 ['O', 'X', 'X', 'O', 'O', 'O', 'O'],
                 ['X', 'X', 'X', 'O', 'O', 'X', 'O'],
                 ['X', ' ', 'X', 'X', 'X', 'X', ' '],
                 ['X', 'O', 'O', 'X', ' ', ' ', 'X'],
                 ['O', 'O', 'X', 'X', ' ', 'X', ' '],
                 ['O', 'X', 'X', 'X', 'O', 'O', 'O'],]
        t = TicTacToe(board)
        self.assertEqual(t.get_best_move(), [3, 1] or [3, 6])
 

if __name__ == "__main__":
    unittest.main()