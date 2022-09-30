from cmath import inf

def getOpenCells(board):  # Required for unit-tests
    free_cells = 0    
    for i in range(len(board)):
        for j in range(len(board)):
            free_cells += board[i][j] == ' '
    return free_cells

class TicTacToe:
    def __init__(self, board = []):
        if board:
            self.board = board
            self.size = len(board)
            self.open_cells = getOpenCells(board)

        else:
            size_str = input("Enter the size of the board (one side): ")
            while not size_str.isdigit():
                size_str = input("Your input is not correct. To set the field size, enter a single integer: ")
            self.size = int(size_str)
            self.open_cells = self.size * self.size
            self.board = self.make_board()
        self.scores = {'X' : 10, 'O' : -10, 'tie': 0}
        self.ai = 'X'
        self.human = 'O'
        self.currentPlayer = self.ai

    def make_board(self):
        return [[' ' for j in range(self.size)] for i in range(self.size)]

    def print_board(self):
        print('    ', end='')
        for k in range (1, self.size + 1):
            print(f'  {k} ', end='')
        print('\n    ', end='')
        print('----' * self.size + '-')
        for i in range(self.size):
            print(f' {i + 1}  | ', end = '')
            for j in range(self.size - 1):
                print(f'{self.board[i][j]} | ', end = '')
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

    def get_winner_small(self):
        #horizontal
        for i in range(self.size):
            row = [self.board[i][j] for j in range(self.size)]
            if self.equals(row):
                return self.board[i][0]

        #vertical
        for j in range(self.size):
            column = [self.board[i][j] for i in range(self.size)]
            if self.equals(column):
                return self.board[0][j]

        #diagonal \
        diagonal_1 = [self.board[i][i] for i in range(self.size)]
        if self.equals(diagonal_1):
            return self.board[0][0]

        #diagonal /
        diagonal_2 = [self.board[i][self.size - i - 1] for i in range(self.size)]
        if self.equals(diagonal_2):
            return self.board[0][self.size - 1]

    def get_winner_large(self):
        IN_ROW = 4
        for i in range(self.size):
            for j  in range(self.size):
                #horizontal
                if j + IN_ROW < self.size:
                    row = [self.board[i][j+k] for k in range(5)]
                    if self.equals(row):
                        return self.board[i][j]

                #vertical
                if i + IN_ROW < self.size:
                    column = [self.board[i+k][j] for k in range(5)]
                    if self.equals(column):
                        return self.board[i][j]

                #diagonal \
                if i + IN_ROW < self.size and j + IN_ROW < self.size:
                    diagonal_1 = [self.board[i+k][j+k] for k in range(5)]
                    if self.equals(diagonal_1):
                        return self.board[i][j]

                #diagonal /
                if i + IN_ROW < self.size and j - IN_ROW >= 0:
                    diagonal_2 = [self.board[i+k][j-k] for k in range(5)]
                    if self.equals(diagonal_2):
                        return self.board[i][j]

    def get_winner(self):
        winner = None
        if self.size >= 5:
            winner = self.get_winner_large()
        else:
            winner = self.get_winner_small()

        if winner is not None:
            return winner
        
        if self.open_cells == 0:
            return "tie"

        return None

    def get_best_move(self):
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
        return move


    def minimax2(self, depth, alpha, beta, isMaximizing):
        if self.size > 3 and depth == 5:
            return (self.scores["tie"])
        result = self.get_winner()
        if result != None:
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

    # Currently not in use (no alpha beta improvements)
    def minimax(self, depth, isMaximizing):
        if self.size > 3 and depth == 5:
            return (self.scores["tie"])
        result = self.get_winner()
        if result != None:
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
            print("\n You go first!")
            t.print_board()

        while self.open_cells > 0:
            if self.currentPlayer == self.human:
                x_str, y_str = input("Your turn: enter the (x, y) coordinates of the cell: ").split()

                # Check if the player entered the correct number
                while not (x_str.isdigit() and not y_str.isdigit()) or \
                    min(x_str, y_str) < 1 or max(x_str, y_str) > self.size:
                    if not (x_str.isdigit() and not y_str.isdigit()):
                        x_str, y_str = input("Input is not correct. Enter integers x, y separated by a space: ").split()
                    else:
                        x_str, y_str = input("The entered values are out of scope for the board size. Enter integers x, y <= board size: ").split()
                
                x, y = map(int, [x_str, y_str])

                # Сhecking that the cell is free
                while self.board[x - 1][y - 1] != ' ':
                     x, y = map(int, input("This cell is already taken! Try again: enter the (x, y) coordinates of the cell: ").split())
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
                self.get_best_move()
                

            self.print_board()
            result = self.get_winner()
            if result == 'tie':
                print("It's a draw!")
            elif result == self.ai:
                print("Oh, you lost. Do you want to try again?")
            elif result == self.human:
                print("Yaay, you won!")
            if result != None:
                return



if __name__ == '__main__':
    while True:
        t = TicTacToe()
        t.play()
        if not input('Do you want to play again? (y/n) ').lower().startswith('y'):
            break
