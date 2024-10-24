# 0x03. Log Parsing

## Description

This project involves writing a Python script that processes real-time log data from `stdin`, computes metrics, and handles interruptions gracefully. The goal is to read log entries line by line, extract relevant information, and print statistics after every 10 lines or when interrupted (CTRL + C).

### Input Format

Each line of the input log follows the format:

```
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```

- **IP Address**: An IP address in the format of 4 numbers between 1 and 255, separated by periods.
- **Date**: The date of the log entry.
- **Status Code**: HTTP status code, one of 200, 301, 400, 401, 403, 404, 405, or 500.
- **File Size**: The size of the file (in bytes) returned by the HTTP request.

If the input format is not valid, the line will be ignored.

### Output

- After every 10 lines, the script will print:
  - **Total File Size**: The sum of all the file sizes in the processed log entries.
  - **Status Code Counts**: The number of occurrences of each valid HTTP status code.

Example output:

```
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
```

- If the script is interrupted with `CTRL + C`, it will print the final statistics before exiting.

### Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/alx-interview.git
   cd alx-interview/0x03-log_parsing
   ```

2. **Run the script**:
   You can either pipe log data from a generator or provide logs through `stdin`.

   **Example 1**: Using a log generator:
   ```bash
   ./0-generator.py | ./0-stats.py
   ```

   **Example 2**: Manual input via `stdin`:
   ```bash
   ./0-stats.py
   ```

   Enter log lines in the specified format. The script will process each line and print metrics accordingly.

### Requirements

- Python 3.4.3+
- The script will be tested on Ubuntu 20.04 LTS.

### Example

Here’s an example of how the script works:

```bash
$ ./0-generator.py | ./0-stats.py
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
```

If interrupted with `CTRL + C`:

```bash
^CFile size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
```

### File Structure

```bash
.
├── 0-generator.py     # Log generator (for testing)
├── 0-stats.py         # Main log parsing script
└── README.md          # Project documentation
```

### Concepts Covered

- File I/O in Python: Reading from `sys.stdin` line by line.
- Signal Handling: Handling keyboard interruption (CTRL + C).
- Data Processing: Parsing and extracting status codes and file sizes.
- Regular Expressions: Validating input format.
- Dictionaries: Counting occurrences of status codes.
- Exception Handling: Managing errors in file reading and data parsing.

### Author

- Mohammad Omar Siddiq
