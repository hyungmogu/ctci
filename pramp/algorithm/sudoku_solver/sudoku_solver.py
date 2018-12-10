import itertools
import os

def sudoku_solve(board):
  if solved(1, board):
    return True
  return False

def solved(idx_subboard, board):
  if idx_subboard > 9:
      return True

  empty_spaces = get_empty_spaces_subboard(idx_subboard, board)
  combinations = get_combinations_subboard(empty_spaces,idx_subboard,board)
  for combination in combinations:
    fill_subboard(board, empty_spaces,combination)
    if not is_placement_subboard_valid(idx_subboard,board) or not is_placement_board_valid(board):
      reset_subboard(empty_spaces,board)
      continue

    if solved(idx_subboard + 1, board):
      return True

    reset_subboard(empty_spaces,board)

  print ('end of combinations reached')
  return False

def is_placement_board_valid(board):
  temp_set = set()

  for idx_row in range(9):
    temp_set = set()
    for idx_col in range(9):
      if board[idx_row][idx_col] != '.' and not board[idx_row][idx_col] in temp_set:
        temp_set.add(board[idx_row][idx_col])
      elif board[idx_row][idx_col] != '.' and board[idx_row][idx_col] in temp_set:
        return False

  for idx_col in range(9):
    temp_set = set()
    for idx_row in range(9):
      if board[idx_row][idx_col] != '.' and not board[idx_row][idx_col] in temp_set:
        temp_set.add(board[idx_row][idx_col])
      elif board[idx_row][idx_col] != '.' and board[idx_row][idx_col] in temp_set:
        return False

  for row in ["".join(x) for x in board]:
    print(row)
  print('------')
  return True

def get_empty_spaces_subboard(idx_subboard, board):
  output = []
  row_start = get_row_start(idx_subboard)
  row_end = row_start + 2
  col_start = get_col_start(idx_subboard)
  col_end = col_start + 2

  for idx_row in range(row_start,row_end+1):
    for idx_col in range(col_start,col_end+1):
      if board[idx_row][idx_col] == '.':
        output.append([idx_row,idx_col])

  return output


def get_row_start(idx_subboard):
  output = -1

  if idx_subboard in [1,2,3]:
    output = 0
  elif idx_subboard in [4,5,6]:
    output = 3
  else:
    output = 6

  return output

def get_col_start(idx_subboard):
  output = -1

  if idx_subboard in [1,4,6]:
    output = 0
  elif idx_subboard in [2,5,8]:
    output = 3
  elif idx_subboard in [3,6,9]:
    output = 6

  return output

def get_combinations_subboard(empty_spaces,idx_subboard,board):
  output = []
  temp_arr = []

  row_start = get_row_start(idx_subboard)
  row_end = row_start + 2
  col_start = get_col_start(idx_subboard)
  col_end = col_start + 2

  for idx_row in range(row_start,row_end+1):
    for idx_col in range(col_start,col_end+1):
      temp_arr.append(board[idx_row][idx_col])

  temp_set = set(temp_arr)
  combinations = list(itertools.permutations(range(1,10),len(empty_spaces)))
  for combination in combinations:
    for value in combination:
      if value in temp_set:
        continue
    output.append(combination)
  return output

def fill_subboard(board, empty_spaces, combination):
  for idx,coord in enumerate(empty_spaces):
    board[coord[0]][coord[1]] = str(combination[idx])

def is_placement_subboard_valid(idx_subboard,board):
  temp_arr = []
  row_start = get_row_start(idx_subboard)
  row_end = row_start + 2
  col_start = get_col_start(idx_subboard)
  col_end = col_start + 2

  for idx_row in range(row_start,row_end+1):
    for idx_col in range(col_start,col_end+1):
      temp_arr.append(board[idx_row][idx_col])

  temp_set = set(temp_arr)

  for value in range(1,10):
    if not str(value) in temp_set:
      return False


  return True

def reset_subboard(empty_spaces,board):
  for coord in empty_spaces:
    board[coord[0]][coord[1]] = '.'


if __name__ == '__main__':
  board = [[".",".",".","7",".",".","3",".","1"],["3",".",".","9",".",".",".",".","."],[".","4",".","3","1",".","2",".","."],[".","6",".","4",".",".","5",".","."],[".",".",".",".",".",".",".",".","."],[".",".","1",".",".","8",".","4","."],[".",".","6",".","2","1",".","5","."],[".",".",".",".",".","9",".",".","8"],["8",".","5",".",".","4",".",".","."]]
  print(sudoku_solve(board))



