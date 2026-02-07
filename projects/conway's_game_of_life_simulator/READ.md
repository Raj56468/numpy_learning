# Conway’s Game of Life – NumPy Implementation

This project is a Python implementation of **Conway’s Game of Life**, created mainly to
**learn and practice NumPy, vectorization, array manipulation, and simulation logic**.

The focus of this project is **understanding the logic**, not building a production-ready
animation or UI.

---

## What is Conway’s Game of Life?

Conway’s Game of Life is a **cellular automaton** where each cell on a grid is either:

- **Alive (1)**
- **Dead (0)**

The grid evolves over time based on simple rules that depend on the number of alive neighbors
around each cell.

---

## Rules

For every cell:

- A **live cell** survives if it has **2 or 3 neighbors**
- A **live cell** dies if it has **fewer than 2 or more than 3 neighbors**
- A **dead cell** becomes alive if it has **exactly 3 neighbors**

All cells update **simultaneously** at each step (generation).

---

## How This Project Works (High Level)

1. A grid of 0s and 1s is created (dead / alive cells)
2. For each generation:
   - Neighbor counts are calculated using NumPy
   - Rules are applied to create a new grid
   - The grid is displayed in the terminal
3. The process repeats for multiple generations

---

## Neighbor Counting Logic (Important Part)

Instead of using nested Python loops, this project uses **NumPy vectorization**:

- The grid is shifted in **8 directions** using `np.roll`
- Each shifted grid aligns neighbors onto the current cell
- All shifted grids are **added together** to get the neighbor count

This approach demonstrates:
- Broadcasting
- Vectorized operations
- Spatial reasoning with arrays

---

## Requirements

- Python 3.x
- NumPy

Install NumPy if needed:
```bash
pip install numpy
