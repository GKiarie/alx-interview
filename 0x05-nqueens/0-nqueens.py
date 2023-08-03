#!/usr/bin/python3
"""N Queens placement on NxN chessboard"""
import sys


def is_safe(board, row, col, N):
    # Check if a queen can be placed in the given cell (row, col)
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(N):
    # Create an empty N x N board
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    def solve(col):
        if col >= N:
            solution = []
            for i in range(N):
                for j in range(N):
                    if board[i][j] == 1:
                        solution.append([i, j])
            solutions.append(solution)
            return True

        for i in range(N):
            if is_safe(board, i, col, N):
                board[i][col] = 1
                solve(col + 1)
                board[i][col] = 0

        return False

    solve(0)

    return solutions


def print_solutions(solutions):
    for solution in sorted(solutions):
        for row, col in solution:
            sys.stdout.write(f"[{row}, {col}] ")
        sys.stdout.write("\n")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    print_solutions(solutions)
