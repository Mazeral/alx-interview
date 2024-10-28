# UTF-8 Validation Module

## Description

This Python module provides functionality to validate UTF-8 encoding by checking if a list of integers represents a valid sequence of UTF-8 encoded bytes. The core of the module is the function `validUTF8`, which verifies the integrity of the byte sequences based on the expected patterns for different types of UTF-8 characters (1-byte, 2-byte, 3-byte, and 4-byte sequences).

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Function Description](#function-description)
- [UTF-8 Encoding Patterns](#utf-8-encoding-patterns)
- [Examples](#examples)
- [License](#license)

## Installation

To use this module, you just need Python installed on your machine. There's no need to install any external dependencies.

## Usage

You can use the `validUTF8` function by passing a list of integers, each representing a byte. The function returns `True` if the list of bytes represents a valid UTF-8 encoding, and `False` otherwise.

### Example:

```python
from validate_utf8 import validUTF8

data = [0xE2, 0x82, 0xAC]  # A valid UTF-8 encoded euro sign (3-byte character)
print(validUTF8(data))  # Output: True

data = [0xF0, 0x90, 0x80]  # Invalid UTF-8 sequence (incomplete 4-byte sequence)
print(validUTF8(data))  # Output: False
```

## Function Description

### `validUTF8(data: list[int]) -> bool`

This function checks if a list of integers (bytes) represents valid UTF-8 encoded characters.

#### Arguments:
- `data (list[int])`: A list of integers, where each integer represents a byte (0 to 255).

#### Returns:
- `bool`: Returns `True` if the list of integers represents a valid UTF-8 sequence, otherwise `False`.

## UTF-8 Encoding Patterns

The module uses predefined patterns to recognize the structure of UTF-8 encoded characters:

- **1-byte** characters: `0xxxxxxx` (fits in 7 bits).
- **2-byte** characters: `110xxxxx 10xxxxxx`.
- **3-byte** characters: `1110xxxx 10xxxxxx 10xxxxxx`.
- **4-byte** characters: `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx`.

The `patterns` dictionary in the module stores the bit patterns for these sequences:

- `1byte`: `0x7F`
- `2b_starter`: `0xC2`
- `2b_c`: `0x80`
- `3b_starter`: `0xE0`
- `3b_c`: `0x80`
- `4b_starter`: `0xF0`
- `4b_c`: `0x80`

## Examples

### Valid UTF-8 Encodings:

1. **1-byte Character**: 
    - Input: `[0x24]` (Dollar sign: `U+0024`)
    - Output: `True`
  
2. **2-byte Character**:
    - Input: `[0xC2, 0xA2]` (Cent sign: `U+00A2`)
    - Output: `True`
  
3. **3-byte Character**:
    - Input: `[0xE2, 0x82, 0xAC]` (Euro sign: `U+20AC`)
    - Output: `True`

### Invalid UTF-8 Encoding:

1. **Invalid Continuation Byte**:
    - Input: `[0xC2, 0x20]` (Second byte is not a valid continuation byte)
    - Output: `False`

## License

This module is open-source and free to use. Feel free to modify and distribute it as per your needs.

---

This README provides an overview of the module, its purpose, and examples of how to use it to validate UTF-8 encodings.
