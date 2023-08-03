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
    for solution in sorted(solutions, key=lambda x: [row for row, col in x]):
        sys.stdout.write("[")
        for i in range(len(solution)):
            sys.stdout.write(f"[{solution[i][0]}, {solution[i][1]}]")
            if i != len(solution) - 1:
                sys.stdout.write(", ")
        sys.stdout.write("]\n")


def check_arguments():
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

    return N


if __name__ == "__main__":
    N = check_arguments()
    solutions = solve_nqueens(N)
    solutions.sort(key=lambda x: x[0][1])
    print_solutions(solutions)
