"""
Author: Nitin Dhiman
"""
from collections import OrderedDict
from collections import namedtuple

GAME_MATRIX = OrderedDict({1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'})


def player_names():
    """
    This function will take an input from the user about the names of the 2 players.
    :return: Name of player 1 and player 2
    """
    player1 = ''
    player2 = ''
    while not player1:
        player1 = input('Enter the name of Player 1: ')
    while not player2:
        player2 = input('Enter the name of Player 2: ')
    return player1, player2


def get_player1_choice(player1):
    """
    This function is used to get choice i.e X/0 from user 1 and set choice of 2nd player accordingly

    :param player1: Name of Player 1
    :return: choice if player 1 and player 2
    """
    choice1 = ''
    while choice1 not in ('x', '0'):
        choice1 = input('%s , enter your choice X or 0: ' % player1).lower()

    if choice1 == 'x':
        choice1 = 'X'
        choice2 = '0'
    else:
        choice2 = 'X'
    return choice1, choice2


def print_canvas():
    """
    Used to print the updated canvas
    :return: NA
    """
    global GAME_MATRIX
    for pos in GAME_MATRIX:
        print('%s  ' % GAME_MATRIX[pos], end='')
        if pos % 3 == 0:
            print()


def get_input(player_data, player_turn):
    """
    This will ask the user for his next move.

    :param player_data: dictionay that contains name and choice of all the players
    :param player_turn: to keep track of turns of the player
    :return: NA
    """
    global GAME_MATRIX
    correct_value_check = False
    while not correct_value_check:
        input_from_player = input('%s, enter the position: ' % player_data[player_turn].name)
        if input_from_player.isdigit():
            input_from_player = int(input_from_player)
            if GAME_MATRIX[input_from_player] == str(input_from_player):
                GAME_MATRIX[input_from_player] = player_data[player_turn].choice
                correct_value_check = True
        else:
            print('Wrong input!!!')


def check_for_win():
    """
    This function will check whether according to current inputs, if any player has won the game.

    :return: NA
    """
    global GAME_MATRIX
    # Horizontal Check
    if GAME_MATRIX[1] == GAME_MATRIX[2] == GAME_MATRIX[3] \
            or GAME_MATRIX[4] == GAME_MATRIX[5] == GAME_MATRIX[6] \
            or GAME_MATRIX[7] == GAME_MATRIX[8] == GAME_MATRIX[9]:
        return True
    # Vertical Check
    elif GAME_MATRIX[1] == GAME_MATRIX[4] == GAME_MATRIX[7] \
            or GAME_MATRIX[2] == GAME_MATRIX[5] == GAME_MATRIX[8] \
            or GAME_MATRIX[3] == GAME_MATRIX[8] == GAME_MATRIX[9]:
        return True
    # Diagonal Check
    elif GAME_MATRIX[1] == GAME_MATRIX[5] == GAME_MATRIX[9] \
            or GAME_MATRIX[3] == GAME_MATRIX[5] == GAME_MATRIX[7]:
        return True
    return False


def play_game(player_data):
    """
    Function that will ask the players to enter their particular inputs.

    :param player_data: dictionay that contains name and choice of all the players
    :return: NA
    """
    player_turn = 'p1'
    for turn in range(1, 10):
        if player_turn == 'p1':
            get_input(player_data, player_turn)
            print_canvas()
            val = check_for_win()
            if val:
                print('Player %s WINS' % player_data[player_turn].name)
                return
            player_turn = 'p2'
        elif player_turn == 'p2':
            get_input(player_data, player_turn)
            print_canvas()
            val = check_for_win()
            if val:
                print('Player %s WINS' % player_data[player_turn].name)
                return
            player_turn = 'p1'
    print('THE MATCH IS DRAW!!!!!\nThanks for playing.')


def start_game():
    """
    This function will keep track of the entire game

    :return: NA
    """
    player_choice = dict()
    names = player_names()
    Player = namedtuple('player_details', ['name', 'choice'])
    choices = get_player1_choice(names[0])
    player_choice['p1'] = Player(names[0], choices[0])
    player_choice['p2'] = Player(names[1], choices[1])
    # print(player_choice)
    print_canvas()
    play_game(player_choice)


if __name__ == '__main__':
    """
    Main function.
    """
    start_game()
