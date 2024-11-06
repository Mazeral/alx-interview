**N Queens Problem**

**Author:** Mohammad Omar Siddiq

**Description:**

The N Queens problem is a classic problem in computer science and mathematics. It involves placing N non-attacking queens on an N×N chessboard. The goal is to find all possible solutions to this problem.

**Usage:**

To run the program, simply call it with the number of queens you want to place as an argument. For example:
```
./0-nqueens.py 4
```
This will print all possible solutions to the 4 Queens problem.

**Input Validation:**

The program will check the input to ensure it is a valid integer greater than or equal to 4. If the input is invalid, the program will print an error message and exit with a status code of 1.

**Output:**

The program will print every possible solution to the problem, one solution per line. Each solution will be represented as a list of pairs, where each pair represents the row and column of a queen on the chessboard.

**Example Output:**

For the 4 Queens problem, the output might look like this:
```
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```
For the 6 Queens problem, the output might look like this:
```
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
```
**Note:**

The program uses the backtracking algorithm to solve the N Queens problem. This algorithm is a recursive algorithm that explores all possible solutions to the problem.

**Required Modules:**

The program only requires the `sys` module to be imported.

I hope this README file helps! Let me know if you have any questions or need further clarification.
