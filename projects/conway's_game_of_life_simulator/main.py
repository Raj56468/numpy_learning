import numpy as np
import time
import os

def initialize_grid(rows, cols, randomize=True):
    if randomize:
        return np.random.randint(2, size=(rows, cols), dtype=np.uint8)
    else:
        return np.zeros((rows, cols), dtype=np.uint8)

def count_neighbors(grid):
    return (
        np.roll(np.roll(grid, 1, 0), 1, 1) +  # top-left
        np.roll(grid, 1, 0) +                 # top
        np.roll(np.roll(grid, 1, 0), -1, 1) + # top-right
        np.roll(grid, -1, 0) +                # bottom
        np.roll(np.roll(grid, -1, 0), 1, 1) + # bottom-left
        np.roll(np.roll(grid, -1, 0), -1, 1) +# bottom-right
        np.roll(grid, 1, 1) +                 # left
        np.roll(grid, -1, 1)                  # right
    )

def update_grid(grid):
    neighbors = count_neighbors(grid)
    # Rule 1 & 3: Any live cell with <2 or >3 neighbors dies
    # Rule 2: Any live cell with 2 or 3 neighbors survives
    # Rule 4: Any dead cell with exactly 3 neighbors becomes alive
    return ((grid == 1) & ((neighbors == 2) | (neighbors == 3))) | ((grid == 0) & (neighbors == 3))

def display_grid(grid):
    for row in grid:
        print("".join("█" if cell else " " for cell in row))
    print("-" * 40)

def run_game(rows=20, cols=40, generations=100, delay=1):
    
    grid = initialize_grid(rows, cols, randomize=True)

    for step in range(generations):
        print("step", step)
        display_grid(grid)
        grid = update_grid(grid).astype(np.uint8)
        time.sleep(delay)

if __name__ == "__main__":
    run_game(rows=20, cols=40, generations=200, delay=1)


