class Board():

    def __init__(self):
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.win = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    def print_board(self):
        print('\n')

        for n in range(len(self.board)):
            board_square = self.board[n]
            if (n + 1) % 3 == 0:
                print(str(board_square))
                if n < 6:
                    print('__|___|__')
            else:
                print(str(board_square) + ' | ', end='')

        print('\n')

    def spaces_left(self):
        free_spaces = list(filter(lambda x: x != 'X' and x != 'O', self.board))
        if len(free_spaces) > 0:
            return False
        return True


class Player():

    def __init__(self):
        self.piece = 'X'
        self.enemy_piece = 'O'
        self.turn = False

    def can_win(self, board, win):
        for check in win:
            win_check = 0
            for m in check:
                if board[m-1] == self.piece:
                    win_check += 1
                    if win_check == 3:
                        return True
        return False

    def player_turn(self, board):
        free_spaces = list(filter(lambda x: x != 'X' and x != 'O', board))
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
                    if win_check == 3:
                        return True
        return False

    def ai_turn(self, board, win):

        free_spaces = list(filter(lambda x: x != 'X' and x != 'O', board))
        print(free_spaces)

        # checks if ai can win and takes spot to ensure this
        for win_line in win:
            ai_win_count = 0
            empty = 10
            for win_number in win_line:
                win_index = win_number - 1

                if board[win_index] == self.piece:
                    ai_win_count += 1
                elif board[win_index] != self.enemy_piece:
                    empty = win_index

            if ai_win_count == 2:
                if empty < 10:
                    return empty

        # checks if player can win and takes spot to stop this
        for win_line in win:
            player_win_count = 0
            empty = 10
            for win_number in win_line:
                win_index = win_number - 1

                if board[win_index] == self.enemy_piece:
                    player_win_count += 1
                elif board[win_index] != self.piece:
                    empty = win_index

            if player_win_count == 2:
                if empty < 10:
                    return empty

        # if middle space is free, select middle
        if 5 in free_spaces:
            return 4

        # if corner space is free, select corner
        if 1 in free_spaces:
            return 0
        if 3 in free_spaces:
            return 2
        if 7 in free_spaces:
            return 6
        if 9 in free_spaces:
            return 8

        # else select middle
        if 2 in free_spaces:
            return 1
        if 4 in free_spaces:
            return 3
        if 6 in free_spaces:
            return 5
        if 8 in free_spaces:
            return 7


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
            game.board.board[game.ai.ai_turn(game.board.board, game.board.win)] = game.ai.piece
            game.board.print_board()
            game.ai.turn = False
            game.player.turn = True
        else:
            print('Player turn')
            game.board.board[game.player.player_turn(game.board.board)] = game.player.piece
            game.board.print_board()
            game.ai.turn = True
            game.player.turn = False

init_game()



