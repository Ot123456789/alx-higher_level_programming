#!/usr/bin/python3
"""
nqueens backtracking program to print the coordinates of n queens
on an nxn grid such that they are all in non-attacking positions
"""

from sys import argv

def print_solution(board):
    """Prints the solution in a readable format"""
    for row in board:
        print(row)

def is_valid(board, row, col, n):
    """Checks if it's valid to place a queen at board[row][col]"""
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col, n):
    """Recursive utility function to solve N Queens problem"""
    if col >= n:
        return True

    for i in range(n):
        if is_valid(board, i, col, n):
            board[i][col] = 1
            if solve_n_queens_util(board, col + 1, n):
                return True
            board[i][col] = 0

    return False

def solve_n_queens(n):
    """Solves the N Queens problem and prints the solution"""
    if n < 4:
        print("N must be at least 4")
        return

    board = [[0 for _ in range(n)] for _ in range(n)]

    if solve_n_queens_util(board, 0, n) is False:
        print("Solution does not exist")
        return

    print_solution(board)

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    
    if not argv[1].isdigit():
        print("N must be a number")
        exit(1)
    
    n = int(argv[1])
    solve_n_queens(n)

