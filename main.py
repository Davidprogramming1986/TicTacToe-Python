import random

class Board(object):

    def __init__(self):
        self.width = 3
        self.height = 3
        self.board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.player_piece = 'X'
        self.ai_piece = 'O'

    def print_board(self):
        for i in range(self.width):
            print('\n')
            for j in range(self.height):
                print(self.board[i][j], end='')
                if j < self.width - 1:
                    print(' | ', end='')
        print('\n')

    def player_move(self, position):
        for i in range(self.width):
            for j in range(self.height):
                if self.board[i][j] == position:
                    self.board[i][j] = self.player_piece
                    return


class AI(object):

    # NO ai in place for choose turn! just a silly test currently in place!

    def __init__(self):
        self.ai_piece = 'O'
        self.player_piece = 'X'

    def choose_turn(self, width, height, board):
        self.free = []
        for i in range(width):
            for j in range(height):
                if board[i][j] != self.player_piece and board[i][j] != self.ai_piece:
                    self.free.append(board[i][j])

        if 5 in self.free:
            board[1][1] = self.ai_piece

        else:
            board[2][2] = self.ai_piece


game_board = Board()
ai = AI()
game_board.print_board()

while True:

    player_move = input('Type in your move >')
    print(player_move)
    game_board.player_move(int(player_move))
    ai.choose_turn(game_board.width, game_board.height, game_board.board)
    game_board.print_board()