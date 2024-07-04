---

# 0x05. N Queens

The "0x05. N Queens" project involves solving the N queens problem using Python. This classic problem challenges you to place N non-attacking queens on an N×N chessboard using the backtracking algorithm.

### Concepts Needed:
- **Backtracking Algorithms**: Understanding how to explore and backtrack through potential solutions.
- **Recursion**: Using recursive functions to implement backtracking.
- **List Manipulations in Python**: Manipulating lists to store queen positions.
- **Python Command Line Arguments**: Handling command-line arguments with the `sys` module.

By mastering these concepts, you'll be equipped to tackle this problem efficiently and learn essential skills in algorithmic thinking and optimization.

### Additional Resources
- Mock Interview

## Requirements
### General
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7.*)
- All your files must be executable

## Tasks
### 0. N Queens
#### Mandatory

The N queens puzzle challenges you to place N non-attacking queens on an N×N chessboard. Write a program that solves this problem.

#### Usage:
```
nqueens N
```
- If the user calls the program with the wrong number of arguments, print `Usage: nqueens N`, followed by a new line, and exit with status 1.
- N must be an integer greater than or equal to 4.
- If N is not an integer, print `N must be a number`, followed by a new line, and exit with status 1.
- If N is smaller than 4, print `N must be at least 4`, followed by a new line, and exit with status 1.
- The program should print every possible solution to the problem, one solution per line, in any order.

#### Example:
```
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```

---