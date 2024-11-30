# 0x08. Making Change

## Description
This project involves solving the classic "minimum coin change problem." The objective is to determine the fewest number of coins needed to meet a specified amount (`total`) using a given set of coin denominations (`coins`). The task must be implemented efficiently due to runtime evaluation requirements.

---

## Prototype
```python
def makeChange(coins, total)
```

### Parameters:
- `coins` (`list` of `int`): A list of positive integers representing the denominations of coins available. You can assume you have an infinite number of each coin.
- `total` (`int`): The target amount for which the minimum number of coins is to be calculated.

### Return:
- The function returns an integer:
  - The fewest number of coins needed to make the `total`.
  - If `total` is 0 or less, return `0`.
  - If the total cannot be reached using the given coins, return `-1`.

---

## Requirements
- The solution must be implemented in Python 3.x.
- Efficiency is critical, as the solution's runtime will be evaluated.

---

## Example Usage
### Input:
```python
coins = [1, 2, 25]
total = 37
```

### Output:
```python
7
```
Explanation: The minimum coins needed are: `25 + 2 + 2 + 2 + 2 + 2 + 2`.

### Another Example:
```python
coins = [1256, 54, 48, 16, 102]
total = 1453
```

Output:
```python
-1
```
Explanation: It is impossible to reach the total of 1453 with the given denominations.

---

## Files
### `0-making_change.py`
Contains the implementation of the `makeChange` function.

### `0-main.py`
A test script to validate the function with sample cases:
```python
#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))  # Expected: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Expected: -1
```

---

## How to Run
1. Clone the repository or copy the code files to your local environment.
2. Run the `0-main.py` file:
   ```bash
   python3 0-main.py
   ```

---

## Edge Cases
- If `total` is `0` or less, the function returns `0` immediately.
- If the list of coins is empty or it’s impossible to reach the `total` using the coins, the function returns `-1`.

---

## Complexity
- **Time Complexity**: \(O(n \cdot t)\), where \(n\) is the number of coin denominations and \(t\) is the `total`.
- **Space Complexity**: \(O(t)\), for the `dp` array used in the solution.

---

## Author
**Mohammad Omar Siddiq**  
