#!/usr/bin/python3

def main():
  # Let's build a really simple Battleship type game with a 10x10 board.
  game_board = build_game_board()
  # Let's hardcode the position of a ship in the fourth row, third column
  game_board[3][2] = 'X'
  print_game_board(game_board)


def build_game_board():
  # Build a 10 x 10 grid. I
  game_board = []
  ships_placed = 0

  # Here, we'll do a nested loop to make 10 rows, and add
  # 10 items in each row.
  for i in range(10):
    game_board.append([])  # Add the empty list
    for j in range(10):
      game_board[i].append(0)
  return game_board

def print_game_board(game_board):
  # Let's loop through the two-dimensional array to
  # print its values.

  # Notice how we are using len(game_board) to control
  # how many times the loop will execute
  for r in range(len(game_board)):
    print('Row {}|'.format(r), end='')

    # Here, we use len(game_board[r]) because we want
    # the length of the list in the first 'row' of game_board
    for c in range(len(game_board[r])):
      print(' {} |'.format(game_board[r][c]), end='')

    print('')

main()
