"""----TIC TAC TIE GAME----"""

"""Mains that will be perfored in the Game"""
# A simple board (3 by 3)
# Display the board
# Playing the Game
# Hold the turn
# Scan for a win
  # scanning the rows
  # scanning the column
  # scanning the diagonals
# Scan for a tie
# Flip between players ("X" or "O")

"""----GLOBAL VARIABLES----"""

# Main board 
board = ["-", "-", "-", 
         "-", "-", "-", 
         "-", "-", "-"]

# if the game is still working
game_working = True

# winner name
winner = None

# Players whose playing
player_playing = "X"

# Main function of all thefunctions collectively
def tictactoe_game():
  
  #display board
  display_board()

  while game_working:
    # hold the turns
    hold_turn(player_playing)

    #checks if game over
    check_if_game_over()

    #flips the players
    flip_players()

    # if the game is ended
  if winner == "X" or winner == "O":
    print(winner + " has won the Game that was coded by Soban")
  elif winner == None:
    print("There is a tie in the Game")



# Function to display the board
def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])


# function to handle the turn
def hold_turn(player_playing):

  print(player_playing + "turn")
  position = input("Choose a point from 1 to 9 on the board:")

  logic = False
  while not logic:
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input(" !!!invalid position!!! choose again:")


    position = int(position) - 1

    if board[position] == "-":
      logic = "True"
    else:
      print("Position already taken")

  board[position] = player_playing

  display_board()

# checks if the player has won or the game is tie
def check_if_game_over():
  check_if_win()
  check_if_tie()

# checks the player has won
def check_if_win():

  # set up global variable in the functions
  global winner

  # checks rows
  row_winner = check_rows()
  # checks columns
  column_winner = check_columns()
  # checks diagonals
  diagonal_winner = check_diagonals() 
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None
  return

# checks for rows
def check_rows():
  # setting up global variable in the function
  global game_working
  # chcks for same values in all rows
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  if row_1 or row_2 or row_3:
    game_working = False
  if row_1:
    return board[1]
  elif row_2:
    return board[4]
  elif row_3:
    return board[7]
  return

# checks for columns
def check_columns():
  # setting up global variable in the function
  global game_working
  # chcks for same values in all columns
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  if column_1 or column_2 or column_3:
    game_working = False
  if column_1:
    return board[3]
  elif column_2:
    return board[4]
  elif column_3:
    return board[5]
  return

# checks for diagnols
def check_diagonals():
  # setting up global variable in the function
  global game_working
  # chcks for same values in all rows
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  if diagonal_1 or diagonal_2:
    game_working = False
  if diagonal_1:
    return board[4]
  elif diagonal_1:
    return board[4]
  return

# checks if the game istie
def check_if_tie():
  global game_working
  global board
  if "-" not in board:
    game_working = False
  return

# flips the players
def flip_players():
  # importing global varibles into function
  global player_playing
  # flips the players
  # if the player_playing was "X" change to player "O"
  if player_playing == "X":
    player_playing = "O"
    # if the current player was "O" then change to player "X"
  elif player_playing == "O":
    player_playing = "X"
  return






# main function that plays the game of tic tac toe
tictactoe_game()
