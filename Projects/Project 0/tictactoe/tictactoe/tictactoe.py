"""
Tic Tac Toe Player
"""

import math
import sys
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    return X if sum([sum(1 for slot in row if slot == None) for row in board])%2==1 else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                moves.add((i, j))
    return moves if len(moves) > 0 else None


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    tempBoard = copy.deepcopy(board) #prevent board container to be permanently changed
    tempBoard[i][j] = player(board)
    return tempBoard

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    def findwinner(board, p):
        for row in board:
            if all(tile==p for tile in row):
                return p
        for i in range(3):
            if all([row[i]==p for row in board]):
                return p 
        if all([board[i][i]==p for i in range(3)]):
            return p
        if all([board[::-1][i][i]==p for i in range(3)]):
            return p
    if findwinner(board, "O") == "O": return "O"
    elif findwinner(board, "X") == "X": return "X"
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if not any([True for row in board if EMPTY in row]) or winner(board) or not actions(board): return True
    return False
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X: return 1
    elif winner(board) == O: return -1
    return 0

def minimax(board):
    if terminal(board): return None
    if player(board) == X:
        next_move = None
        if terminal(board): return next_move
        best = -999999
        for action in actions(board):
            move_value = minimize(result(board, action))
            if move_value > best:
                next_move = action
        return next_move
    else: 
        next_move = None
        if terminal(board): return next_move
        best = 999999
        for action in actions(board):
            move_value = maximize(result(board, action))
            if move_value < best:
                next_move = action
        return next_move

def minimize(board):
    if terminal(board):
        return utility(board)
    val = 999
    for action in actions(board):
        val = min(val, maximize(result(board, action)))
        if val == -1: break #it will not get better than -1
    return val

def maximize(board):
    if terminal(board):
        return utility(board)
    val = -999
    for action in actions(board):
        val = max(val, minimize(result(board, action)))
        if val == 1: break #it will not get better than 1 
    return val
    