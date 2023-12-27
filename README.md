# Sudoku Solver in Python

This project is a Python implementation of a Sudoku solver. It provides functionality to solve Sudoku puzzles of varying complexities.
It also provides an UI to enter the unsolved puzzle and use the required funciton to solve the puzzle.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Overview

This Sudoku solver project is developed in Python and aims to solve Sudoku puzzles of different difficulty levels. It offers an efficient backtracking algorithm to find the solution to any valid Sudoku grid.

## Features

- Solves Sudoku puzzles of varying complexities.
- Simple and easy-to-understand Python implementation.
- Provides UI using Tkinter for user friendly interface alongwith commandline support.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/rohi-s/sudoku-solver.git
   ```

2. Navigate to the project directory:

   ```bash
   cd sudoku-solver
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use the Sudoku solver, you can either import the solve function into your Python script or run the solver directly from the command line or use the solver_ui.py to get the user interface window to enter the puzzle.

### Running from Command Line

```bash
python python -c 'import solve; print(solve.solve(<array_of_unsolved_puzzle>))'
```

Replace `<array_of_unsolved_puzzle>` with the path to the file containing the Sudoku puzzle to solve.

### Importing in Python

```python
from solve import solve

# Use solve function with your Sudoku grid as input
# Example: solved_grid = solve(your_input_grid)
```

## Example

To solve a Sudoku puzzle using this solver from the command line:

```bash
python -c 'import solve,puzzles; print(solve.solve(puzzles.easy))'
```

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/your-feature`).
6. Create a new Pull Request.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify this code according to the terms of this license.

---

