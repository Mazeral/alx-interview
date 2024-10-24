#!/usr/bin/python3
import sys
import re

# Initialize metrics
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
count = 0

log_format = r'^\S+ - \[\S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'


def print_metrics(total_size, status_codes):
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


try:
    for line in sys.stdin:
        match = re.match(log_format, line)
        if match:
            # Extract status code and file size
            status_code = int(match.group(1))
            file_size = int(match.group(2))

            # Update total file size and status code count
            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1

            count += 1

            # Print metrics every 10 lines
            if count % 10 == 0:
                print_metrics(total_size, status_codes)

except KeyboardInterrupt:
    # Print final statistics when interrupted
    print_metrics(total_size, status_codes)
    raise
