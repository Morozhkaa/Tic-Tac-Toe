import unittest
from main import TicTacToe 

class Test_TicTacToe(unittest.TestCase):


    # 1. Checking the "equals" function
    def test_equals_func(self):
        t = TicTacToe([' ']) # Stub 
        self.assertTrue(isFilled(['X', 'X', 'X', 'X']))
        self.assertTrue(isFilled(['O', 'O', 'O', 'O']))

        self.assertFalse(isFilled(['X', 'X', ' ', 'X']))
        self.assertFalse(isFilled(['X', 'X', 'O', 'O']))
        


    # 2. Checking the "checkWinner" function

        # 2.1 Checking when field sizes <= 5

    def test_main_diagonal_is_winner_size3(self):
        board = [['X', 'O', 'O'],
                 ['O', 'X', 'X'],
                 [' ', ' ', 'X']]
        t = TicTacToe(board)
        self.assertEqual(t.checkWinner(), 'X')

    def test_secondary_diagonal_is_winner_size4(self):
        board = [['O', ' ', ' ', 'X'],
                 ['O', 'O', 'X', ' '],
                 [' ', 'X', ' ', ' '],
                 ['X', ' ', ' ', ' ']]
        t = TicTacToe(board)
        self.assertEqual(t.checkWinner(), 'X')

    def test_second_column_is_winner_size4(self):
        board = [['O', 'O', ' ', 'X'],
                 ['X', 'O', 'O', 'X'],
                 ['X', 'O', 'X', 'X'],
                 ['X', 'O', ' ', 'O']]
        t = TicTacToe(board)
        self.assertEqual(t.checkWinner(), 'O')

    def test_third_row_is_winner_size5(self):
        board = [['O', 'X', 'X', 'X', ' '],
                 ['X', 'X', 'O', 'X', 'X'],
                 ['O', 'O', 'O', 'O', 'O'],
                 ['X', 'O', 'X', 'O', ' ']]
        t = TicTacToe(board)
        self.assertEqual(t.checkWinner(), 'O')


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
        self.assertEqual(t.checkWinner(), 'O')

    def test_second_row_is_winner_size7(self):
        board = [['X', 'X', 'X', 'X', 'O', 'O', ' '],
                 ['O', 'X', 'X', 'X', 'X', 'X', 'O'],
                 ['O', ' ', ' ', 'X', ' ', 'O', ' '],
                 ['X', ' ', 'X', ' ', ' ', 'O', ' '],
                 ['O', 'X', ' ', 'O', ' ', ' ', ' '],
                 ['X', 'O', 'O', 'O', ' ', ' ', ' '],
                 ['O', ' ', ' ', 'O', ' ', ' ', ' '],]
        t = TicTacToe(board)
        self.assertEqual(t.checkWinner(), 'X')

    def test_secondary_diagonal_is_winner_size7(self):
        board = [['X', 'X', 'X', 'X', 'O', 'O', ' '],
                 ['O', ' ', ' ', 'X', 'X', ' ', ' '],
                 ['O', ' ', ' ', 'X', ' ', ' ', ' '],
                 ['X', ' ', 'X', ' ', ' ', ' ', ' '],
                 ['O', 'X', ' ', 'O', ' ', ' ', ' '],
                 ['X', 'O', 'O', 'O', ' ', ' ', ' '],
                 ['O', ' ', ' ', 'O', ' ', ' ', ' '],]
        t = TicTacToe(board)
        self.assertEqual(t.checkWinner(), 'X')

    def test_main_diagonal_is_winner_size7(self):
        board = [['X', 'X', 'X', 'X', 'O', ' ', ' '],
                 ['O', ' ', ' ', 'X', 'X', ' ', ' '],
                 ['O', 'O', ' ', 'X', ' ', ' ', ' '],
                 ['O', 'X', 'O', 'X', 'X', 'X', ' '],
                 ['O', 'O', ' ', 'O', ' ', ' ', ' '],
                 ['X', 'O', 'O', 'O', 'O', ' ', ' '],
                 ['O', ' ', ' ', 'O', 'X', ' ', ' '],]
        t = TicTacToe(board)
        self.assertEqual(t.checkWinner(), 'O')

    def test_tie_size7(self): # No free cells, no winners -> tie
        board = [['X', 'X', 'X', 'X', 'O', 'O', 'X'],
                 ['O', 'X', 'X', 'X', 'X', 'O', 'O'],
                 ['O', 'O', 'O', 'X', 'O', 'O', 'X'],
                 ['O', 'X', 'O', 'X', 'O', 'X', 'O'],
                 ['O', 'O', 'X', 'O', 'X', 'X', 'X'],
                 ['X', 'O', 'X', 'O', 'X', 'O', 'X'],
                 ['O', 'O', 'X', 'O', 'X', 'O', 'X'],]
        t = TicTacToe(board)
        self.assertEqual(t.checkWinner(), "tie")

    def test_NULL_size7(self): # There are no winners, the game continues
        board = [['X', 'X', 'X', 'X', 'O', ' ', ' '],
                 ['O', ' ', ' ', 'X', 'X', ' ', ' '],
                 ['O', 'O', ' ', 'X', ' ', ' ', ' '],
                 ['O', 'X', 'O', 'X', 'X', 'X', ' '],
                 ['O', 'O', ' ', 'O', ' ', ' ', ' '],
                 ['X', 'O', 'O', 'O', 'X', ' ', ' '],
                 ['O', ' ', ' ', 'O', 'X', 'O', ' '],]
        t = TicTacToe(board)
        self.assertEqual(t.checkWinner(), None) 



    # 3. Checking the best move

    def test_bestMove1_size4(self):
        board = [['O', ' ', ' ', 'X'],
                 ['O', 'O', 'X', ' '],
                 [' ', 'X', ' ', ' '],
                 [' ', ' ', ' ', ' ']]
        t = TicTacToe(board)
        self.assertEqual(t.bestMove(), (3, 0))

    def test_bestMove2_size4(self):
        board = [['O', 'X', ' ', 'X'],
                 ['O', 'O', 'O', ' '],
                 ['X', 'X', 'X', ' '],
                 ['O', ' ', ' ', ' ']]
        t = TicTacToe(board)
        self.assertEqual(t.bestMove(), (2, 3))

    def test_bestMove3_size4(self):
        board = [['O', 'X', ' ', 'X'],
                 ['O', 'O', 'O', ' '],
                 ['X', 'X', ' ', ' '],
                 ['O', ' ', 'X', ' ']]
        t = TicTacToe(board)
        self.assertEqual(t.bestMove(), (1, 3))

    def test_bestMove4_size5(self):
        board = [['O', 'X', 'X', 'X', ' '],
                 ['O', 'X', 'X', 'O', 'O'],
                 ['X', 'X', 'O', 'X', 'O'],
                 ['O', 'O', 'O', 'X', 'O'],
                 ['O', 'X', ' ', 'X', ' '],]
        t = TicTacToe(board)
        self.assertEqual(t.bestMove(), (0, 4))

    def test_bestMove5_size7(self):
        board = [['O', 'O', 'O', 'O', 'X', 'O', 'X'],
                 ['O', 'X', 'X', 'O', 'O', 'O', 'O'],
                 ['X', 'X', 'X', 'O', 'O', 'X', 'O'],
                 ['X', ' ', 'X', 'X', 'X', 'X', ' '],
                 ['X', 'O', 'O', 'X', ' ', ' ', 'X'],
                 ['O', 'O', 'X', 'X', ' ', 'X', ' '],
                 ['O', 'X', 'X', 'X', 'O', 'O', 'O'],]
        t = TicTacToe(board)
        self.assertEqual(t.bestMove(), (3, 1) or (3, 6))
 

if __name__ == "__main__":
    unittest.main()
