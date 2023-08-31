#!/usr/bin/python3
"""
island-perimeter task
"""


def island_perimeter(grid):
    """
    returns the perimeter of the island described in grid
    """
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4  # Initialize with 4 sides

                # Check left neighbor
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2

                # Check upper neighbor
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2

    return perimeter
