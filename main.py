from asyncio.windows_events import NULL
from cmath import inf


class TicTacToe:
    def __init__(self):
        size_str = input(" Enter the size of the board (one side):  ")
        while not size_str.isdigit():
            size_str = input(" Your input is not correct. To set the field size, enter a single integer:  ")
        self.size = int(size_str)
        self.scores = {'X' : 10, 'O' : -10, 'tie': 0}
        self.open_cells = self.size * self.size
        self.board = self.make_board()
        self.ai = 'X'
        self.human = 'O'
        self.currentPlayer = self.ai

    def make_board(self):
        return [[' ' for j in range(self.size)] for i in range(self.size)]

    def print_board(self):
        print('    ', end='')
        for k in range (1, self.size + 1):
            print('  ', k, ' ', sep='', end='')
        print('\n    ', end='')
        print('----' * self.size + '-')
        for i in range(self.size):
            print(' ', i + 1, '  | ', sep = '', end = '')
            for j in range(self.size - 1):
                print(self.board[i][j], ' | ', sep='', end = '')
            print(self.board[i][self.size - 1], '|')
            print('    ', end = '')
            print('----' * self.size + '-')
        print()

    def equals(self, args):
        cur = args[0]
        for arg in args:
            if arg != cur:
                return False
        return cur != ' '

    def checkWinner(self):
        #border = min(self.size, 5)
        if self.size > 5:
            for i in range(self.size):
                for j  in range(self.size):
                    #horizontal
                    if j + 4 <= self.size - 1:
                        arr = [self.board[i][j+k] for k in range(5)]
                        if self.equals(arr):
                            return self.board[i][j]
                    #vertical
                    if i + 4 <= self.size - 1:
                        arr = [self.board[i+k][j] for k in range(5)]
                        if self.equals(arr):
                            return self.board[i][j]
                    #diagonal
                    if i + 4 <= self.size - 1 and j + 4 <= self.size - 1:
                        arr = [self.board[i+k][j+k] for k in range(5)]
                        if self.equals(arr):
                            return self.board[i][j]
                    if i + 4 <= self.size - 1 and j - 4 >= 0:
                        arr = [self.board[i+k][j-k] for k in range(5)]
                        if self.equals(arr):
                            return self.board[i][j]
        else:
            #horizontal
            for i in range(self.size):
                arr = [self.board[i][j] for j in range(self.size)]
                if self.equals(arr):
                    return self.board[i][0]
            #vertical
            for j in range(self.size):
                arr = [self.board[i][j] for i in range(self.size)]
                if self.equals(arr):
                    return self.board[0][j]
            #diagonal
            arr = [self.board[i][i] for i in range(self.size)]
            if self.equals(arr):
                return self.board[0][0]
            arr = [self.board[i][self.size - i - 1] for i in range(self.size)]
            if self.equals(arr):
                return self.board[0][self.size - 1]

        if self.open_cells == 0:
            return "tie"
        return NULL

    def bestMove(self):
        bestScore = -inf
        move = [-1, -1]
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == ' ':
                    self.board[i][j] = self.ai
                    self.open_cells -= 1
                    #score = self.minimax(0, False)
                    score = self.minimax2(0, -inf, inf, False)
                    self.board[i][j] = ' '
                    self.open_cells += 1
                    if score > bestScore:
                        bestScore = score
                        move = [i, j]
        self.board[move[0]][move[1]] = self.ai
        self.open_cells -= 1
        self.currentPlayer = self.human


    def minimax2(self, depth, alpha, beta, isMaximizing):
        if self.size > 3 and depth == 5:
            return (self.scores["tie"])
        result = self.checkWinner()
        if result != NULL:
            return self.scores[result]
      
        if isMaximizing:
            bestScore = -inf
            for i in range(self.size):
                for j in range(self.size):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = self.ai
                        self.open_cells -= 1
                        score = self.minimax2(depth + 1, alpha, beta, False)
                        self.board[i][j] = ' '
                        self.open_cells += 1
                        bestScore = max(score, bestScore)
                        alpha = max(alpha, bestScore)
                        if alpha >= beta:
                            break
            return bestScore
        else:
            bestScore = inf
            for i in range(self.size):
                for j in range(self.size):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = self.human
                        self.open_cells -= 1
                        score = self.minimax2(depth + 1, alpha, beta, True)
                        self.board[i][j] = ' '
                        self.open_cells += 1
                        bestScore = min(score, bestScore)
                        beta = min(beta, bestScore)
                        if beta <= alpha:
                            break
            return bestScore

    # no alpha beta improvements
    def minimax(self, depth, isMaximizing):
        if self.size > 3 and depth == 5:
            return (self.scores["tie"])
        result = self.checkWinner()
        if result != NULL:
            return self.scores[result]
        if isMaximizing:
            bestScore = -inf
            for i in range(self.size):
                for j in range(self.size):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = self.ai
                        self.open_cells -= 1
                        score = self.minimax(depth + 1, False)
                        self.board[i][j] = ' '
                        self.open_cells += 1
                        bestScore = max(score, bestScore)
            return bestScore
        else:
            bestScore = inf
            for i in range(self.size):
                for j in range(self.size):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = self.human
                        self.open_cells -= 1
                        score = self.minimax(depth + 1, True)
                        self.board[i][j] = ' '
                        self.open_cells += 1
                        bestScore = min(score, bestScore)

            return bestScore
   

    def play(self):
   
        if input(' Will you start the game? (y/n) ').lower().startswith('y'):
            # Who goes first plays for "X", so we change some parameters
            self.human = 'X'
            self.ai = 'O'
            self.scores = {'O' : 10, 'X' : -10, 'tie': 0}
            self.currentPlayer = self.human
            print("\n You go first! ")
            t.print_board()

        while self.open_cells > 0:
            if self.currentPlayer == self.human:
                x_str, y_str = input(" Your turn: enter the (x, y) coordinates of the cell:  ").split()

                # Check if the player entered the correct number
                while (not x_str.isdigit()) or (not y_str.isdigit() or int(x_str) > self.size or int(y_str) > self.size):
                    if (not x_str.isdigit()) or (not y_str.isdigit()):
                        x_str, y_str = input(" Input is not correct. Enter integers x, y separated by a space:  ").split()
                    else:
                        x_str, y_str = input(" The entered values are out of scope for the board size. Enter integers x, y <= board size:  ").split()
                x, y = map(int, [x_str, y_str])

                # Сhecking that the cell is free
                while self.board[x - 1][y - 1] != ' ':
                     x, y = map(int, input(" This cell is already taken! Try again: enter the (x, y) coordinates of the cell:  ").split())
                self.board[x - 1][y - 1] = self.human
                self.currentPlayer = self.ai
                self.open_cells -= 1
            else:
                # сrutch to make the first move of the computer faster
                if self.open_cells == self.size * self.size:
                    self.board[0][0] = self.ai
                    self.currentPlayer = self.human
                    self.open_cells -= 1
                    self.print_board()
                    continue
                self.bestMove()
                

            self.print_board()
            result = self.checkWinner()
            if result == 'tie':
                print("It's a draw!")
            elif result == self.ai:
                print("Oh, you lost. Do you want to try again?")
            elif result == self.human:
                print("Yaay, you won!")
            if result != NULL:
                return



if __name__ == '__main__':
    while True:
        t = TicTacToe()
        t.play()
        if not input('Do you want to play again? (y/n) ').lower().startswith('y'):
            break
