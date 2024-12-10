# 0x0A. Prime Game

## Problem Description

Maria and Ben are playing a game using sets of consecutive integers starting from 1 to `n`. The rules are as follows:

1. Maria always goes first.
2. On each turn, a player chooses a prime number from the set and removes it, along with all its multiples, from the set.
3. The player who cannot make a move loses the game.

The game is played over `x` rounds, where each round has its own value of `n`. Your task is to determine the winner of the most rounds, assuming both players always play optimally.

## Prototype

```python
def isWinner(x, nums):
```

- `x` is the number of rounds.
- `nums` is a list of integers, where each integer represents the value of `n` for a specific round.
- Returns the name of the player (`"Maria"` or `"Ben"`) who wins the most rounds. If the result is a tie, return `None`.

## Constraints

- `1 <= x <= 10,000`
- `1 <= n <= 10,000`
- No external libraries or packages may be imported.

## Example

Given `x = 3` and `nums = [4, 5, 1]`:

### Round 1: n = 4

- Maria picks `2` and removes `{2, 4}`. Remaining set: `{1, 3}`.
- Ben picks `3` and removes `{3}`. Remaining set: `{1}`.
- Maria cannot make a move. **Ben wins this round**.

### Round 2: n = 5

- Maria picks `2` and removes `{2, 4}`. Remaining set: `{1, 3, 5}`.
- Ben picks `3` and removes `{3}`. Remaining set: `{1, 5}`.
- Maria picks `5` and removes `{5}`. Remaining set: `{1}`.
- Ben cannot make a move. **Maria wins this round**.

### Round 3: n = 1

- There are no prime numbers. Maria cannot make a move. **Ben wins this round**.

### Result: 

- Maria: 1 win
- Ben: 2 wins

**Output**: `"Ben"`

### Execution Example

```bash
$ cat main_0.py
#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
$ ./main_0.py
Winner: Ben
```

## Repository Structure

- **GitHub Repository**: `alx-interview`
- **Directory**: `0x0A-primegame`
- **File**: `0-prime_game.py`

## Requirements

- Code must be written in Python 3.
- Follow Python style guidelines (`pycodestyle`).
- Optimize for performance, given the constraints of the problem.
