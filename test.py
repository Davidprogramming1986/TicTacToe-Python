board = [0, 1, 'O', 3, 'X', 5, 6, 7, 'X']

free_spaces = list(filter(lambda x: x != 'X' and x != 'O', board))

free_spaces = list(filter(lambda x: x != 'X' and x != 'O', board))

while True:
    print(free_spaces)
    player_choice = input('Select your square > ')
    player_choice = int(player_choice)
    print(type(player_choice))
    if player_choice in free_spaces:
        break
