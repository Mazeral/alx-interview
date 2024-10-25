#!/usr/bin/python3
"""
Module of log parsing.

Parses log input from stdin, collecting metrics on file size and
HTTP status codes. Prints statistics every 10 lines or upon
receiving a SIGINT signal.
"""

import sys
import re
import signal
from collections import defaultdict

def signal_handler(sig, frame):
    """
    Signal handler for SIGINT (CTRL + C).

    Prints current statistics before exiting.
    """
    print_stats()
    sys.exit(0)

# Register signal handler for SIGINT
signal.signal(signal.SIGINT, signal_handler)

# Initialize metrics
total_file_size = 0  # Total file size in bytes
status_code_counts = defaultdict(int)  # Status code occurrence counts
line_count = 0  # Number of lines processed

# Regular expression pattern for log line format
pattern = re.compile(
    r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # IP address
    r" - \[(.*?)\] \"GET /projects/260 HTTP/1.1\" "  # Date and request
    r"(\d{3}) (\d+)$"  # Status code and file size
)

def process_stdin():
    """
    Reads from stdin line by line, processing each log entry.
    """
    global line_count
    for line in sys.stdin:
        line_count += 1
        process_log_line(line)

def process_log_line(line):
    """
    Attempts to match and process a single log line.

    Updates metrics if the line matches the expected format.
    """
    match = pattern.match(line)
    if match:
        # Extract relevant data
        _, _, status_code, file_size = match.groups()
        status_code, file_size = int(status_code), int(file_size)

        # Update metrics
        global total_file_size, status_code_counts
        total_file_size += file_size
        status_code_counts[status_code] += 1

    # Print statistics every 10 lines or upon signal
    if line_count % 10 == 0:
        print_stats()

def print_stats():
    """
    Prints the collected statistics.

    Includes total file size and counts for specific HTTP status codes.
    """
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_code_counts):
        if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
            print(f"{status_code}: {status_code_counts[status_code]}")

if __name__ == "__main__":
    process_stdin()
    # Print final statistics (if not exited by signal)
    print_stats()
