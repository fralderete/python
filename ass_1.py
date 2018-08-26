import random

# print('\n'*100)       # Clear screen

def display_board(board):
    print('\n')
    print(board[7], "|", board[8], "|", board[9])
    print("----------")
    print(board[4], "|", board[5], "|", board[6])
    print("----------")
    print(board[1], "|", board[2], "|", board[3])
    print("\n")

''' When an argument is passed to pos as a list it will take that argument at that position and 
    display it on the 'board'. I'm thinking I'll write a while loop that will take inputs from 
    the players and have it quit once the board is full. My next problem is having the program
    recognize when one player wins. I can use if statements but it will be a long program. I also
    should have the player only pick position, and not input an X or O so they don't enter some
    random long string and ruin the game. 
'''

# Some direction for the player so they know what numbers to pick

ex_inputs = [0,1,2,3,4,5,6,7,8,9]
display_board(ex_inputs)
print('When making selections on position the above is what the board will accept.')

def player_input():     # This function commands the first player to pick his letter of choice.
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()
                        # .upper() is used so whenever the player picks, using a capitalized or lowercase letter
                        # won't break the game.
    if marker == 'X':
        return ('X', 'O')
    else:               # tuples are returned that will be fed to a player1 or p2 later
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker
                        # This function is used to place the marker on the board in a certain position (1-9)

def win_check(board, mark):     # This checks every possible combination for the game
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal

# win_check(inputs,'X')

def choose_first():     # Simple function to choose between 0-1 to select who goes first
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def space_check(board, position):   # Checks to make sure a spot on the board is open by taking the players input
    return board[position] == ' '


def full_board_check(board):        # Checks to see if the board is full using range
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):           # Function to make player choose position
    position = 0                    # sets local variable to 0 to be used below

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
                                    # If a position is open ask for the input
    return position


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
                                    # Resets game (Don't know where this leads quite yet)

print('Welcome to Tic Tac Toe!')

''' Below is the actual code for the game after all of the checks. 
'''

while True:                 # While True guarantees this runs continuously
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    # This one confused me a lot, but what it is doing is taking the tuple that was returned at player_input()
    # and assigning the "X" and "O" to p1 and p2
    turn = choose_first()
    # Uses the random function generated above to pick who goes first
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No.')
    # A simple input that asks if you're ready to play
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    # Any answer that has an upper or lowercase 'Y' at [0] will activate the game. Any other input breaks the game.
    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            display_board(theBoard)     # Clears the board from any previous inputs
            position = player_choice(theBoard)  # The position picked by the player is gathered from the players choice
            place_marker(theBoard, player1_marker, position)    # Marker is placed

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
                # If you get one of the winning conditions the game ends and you get a congrats message
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!') #If the board is full without a win condition the game draws and quits
                    break
                else:
                    turn = 'Player 2'   # If no one has won after player 1s turn go to player 2

        else:
            # Player2's turn. Same comments as above.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():    # If you choose no when it asks to replay the game it breaks.
        break