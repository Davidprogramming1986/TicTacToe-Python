import random

class Board():

    def __init__(self):
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
        self.win = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [1, 6, 11, 16, 21], [2, 7, 12, 17, 22], [3, 8, 13, 18, 23], [4, 9, 14, 19, 24], [5, 10, 15, 20, 25], [1, 7, 13, 19, 25], [5, 9, 13, 17, 21]]

    def print_board(self):
        print('\n')

        for n in range(len(self.board)):
            board_square = self.board[n]
            if (n + 1) % 5 == 0:
                print(str(board_square))
                if n < 20:
                    print('___|____|____|____|___')
            else:
                if n <= 9:
                    print(str(board_square) + '  | ', end='')
                else:
                    print(str(board_square) + ' | ', end='')

        print('\n')

    def spaces_left(self):
        free_spaces = list(filter(lambda x: x != 'X' and x != 'O' and x != 'O ' and x != 'X ', self.board))
        if len(free_spaces) > 0:
            return False
        return True


class Player():

    def __init__(self):
        self.piece = 'X'
        self.enemy_piece = 'O'
        self.turn = False

    def can_win(self, board, win):
        win_check = 0
        for check in win:
            win_check = 0
            for m in check:
                if board[m-1] == self.piece:
                    win_check += 1
                    if win_check == 5:
                        return True
        return False

    def player_turn(self, board):
        free_spaces = list(filter(lambda x: x != 'X' and x != 'O' and x != 'O ' and x != 'X ', board))
        while True:
            print(free_spaces)
            player_choice = input('Select your square > ')
            player_choice = int(player_choice) - 1
            if (player_choice + 1) in free_spaces:
                return player_choice

            print('You need to select a valid choice')


class AI():

    def __init__(self):
        self.piece = 'O'
        self.enemy_piece = 'X'
        self.turn = True

    def can_win(self, board, win):
        for check in win:
            win_check = 0
            for m in check:
                if board[m-1] == self.piece:
                    win_check += 1
                    if win_check == 5:
                        return True
        return False

    def ai_turn(self, board, win):

        free_spaces = list(filter(lambda x: x != 'X' and x != 'O' and x != 'O ' and x != 'X ', board))
        print(free_spaces)

        # checks if ai can win and takes spot to stop this
        for win_line in win:
            ai_win_count = 0
            empty = 26
            for win_number in win_line:
                win_index = win_number - 1

                if board[win_index] == self.piece:
                    ai_win_count += 1
                elif board[win_index] != self.enemy_piece:
                    empty = win_index

            if ai_win_count == 4:
                print('empty = ', empty)
                if empty < 26:
                    return empty

        # checks if player can win and takes spot to stop this
        for win_line in win:
            player_win_count = 0
            empty = 26
            for win_number in win_line:
                win_index = win_number - 1

                if board[win_index] == self.enemy_piece:
                    player_win_count += 1
                elif board[win_index] != self.piece:
                    empty = win_index

            if player_win_count == 4:
                if empty < 26:
                    return empty

        # if middle space is free, select middle
        if 13 in free_spaces:
            return 12

        # if corner space is free, select corner
        if 1 in free_spaces:
            return 0
        if 5 in free_spaces:
            return 4
        if 21 in free_spaces:
            return 20
        if 25 in free_spaces:
            return 24

        # else select inner middle corners
        if 7 in free_spaces:
            return 6
        if 9 in free_spaces:
            return 8
        if 17 in free_spaces:
            return 16
        if 19 in free_spaces:
            return 18

        # if none of these criteria met, pick a random free space
        return random.choice(free_spaces) - 1

class Game():

    def __init__(self):
        self.board = Board()
        self.player = Player()
        self.ai = AI()

    def choose_piece(self):

        while True:
            player_choice = input('Choose your piece, O or X > ')
            player_choice = player_choice.upper()
            if player_choice != 'O' and player_choice != 'X':
                print('Wrong Choice, you need to select either X or O, please try again')
                continue
            if player_choice == 'X':
                print('You have selected X')
                self.player.piece = 'X'
                self.player.enemy_piece = 'O'
                self.ai.piece = 'O'
                self.ai.enemy_piece = 'X'
                self.ai.turn = False
                self.player.turn = True
                break
            else:
                print('You have selected O')
                self.player.piece = 'O'
                self.player.enemy_piece = 'X'
                self.ai.piece = 'X'
                self.ai.enemy_piece = 'O'
                self.ai.turn = True
                self.player.turn = False
                break


def init_game():

    # instantiates the game
    game = Game()

    # player chooses their piece, ai to get other option (choice is X or O)
    game.choose_piece()

    # prints gameboard
    print('Starting board')
    game.board.print_board()

    # game loop
    while True:

        # checks for a full board
        if game.board.spaces_left():
            print('The game is a draw, game over')
            break

        # checks if player has won
        if game.player.can_win(game.board.board, game.board.win):
            print('Player Wins!')
            break

        #checks if ai has won
        if game.ai.can_win(game.board.board, game.board.win):
            print('AI Wins')
            break

        # if ai is X, ai goes first
        if game.ai.turn:
            print('AI turn')
            go = game.ai.ai_turn(game.board.board, game.board.win)
            if go < 10:
                game.board.board[go] = game.ai.piece
            else:
                game.board.board[go] = game.ai.piece + ' '
            game.board.print_board()
            game.ai.turn = False
            game.player.turn = True
        else:
            print('Player turn')
            go = game.player.player_turn(game.board.board)
            if go < 10:
                game.board.board[go] = game.player.piece
            else:
                game.board.board[go] = game.player.piece + ' '
            game.board.print_board()
            game.ai.turn = True
            game.player.turn = False

init_game()



