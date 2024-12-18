**Minimum Operations**
=====================

**Author:** Mohammad Omar Siddiq

**Task Description:**
-------------------

In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

**Prototype:**
-------------

`def minOperations(n)`

**Returns:**
------------

* An integer representing the minimum number of operations needed to reach n H characters.
* If n is impossible to achieve, return 0.

**Example:**
------------

`n = 9`

`H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH`

`Number of operations: 6`

**Testing:**
-------------

The `0-main.py` file provides a test case for the `minOperations` function.

**Repo:**
---------

* GitHub repository: alx-interview
* Directory: 0x02-minimum_operations
* File: 0-minoperations.py
