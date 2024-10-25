#!/usr/bin/python3
"""
Module of log parsing
"""
import sys
import re
import signal
from collections import defaultdict


# Define the signal handler for CTRL + C
def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)


# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

# Initialize metrics
total_file_size = 0
status_code_counts = defaultdict(int)
line_count = 0

# Regular expression pattern to match the input format
pattern = re.compile
(r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\
        - \[(.*?)\] \"GET /projects/260 HTTP/1.1\" (\d{3}) (\d+)$")

# Read from stdin line by line
for line in sys.stdin:
    line_count += 1

    # Try to match the input format
    match = pattern.match(line)
    if match:
        # Extract relevant data
        _, _, status_code, file_size = match.groups()
        status_code, file_size = int(status_code), int(file_size)

        # Update metrics
        total_file_size += file_size
        status_code_counts[status_code] += 1

    # Print statistics every 10 lines or upon signal
    if line_count % 10 == 0:
        print_stats()

# Print final statistics (if not exited by signal)
print_stats()


# Define a function to print the collected statistics
def print_stats():
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_code_counts):
        if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
            print(f"{status_code}: {status_code_counts[status_code]}")
