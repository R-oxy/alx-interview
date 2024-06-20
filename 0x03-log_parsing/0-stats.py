#!/usr/bin/python3
""" 0-stats.py """

import sys
import signal

# Initialize variables
total_file_size = 0
status_code_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0


def print_stats():
    """Print the current statistics."""
    print("File size: {}".format(total_file_size))
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print("{}: {}".format(code, status_code_counts[code]))


def signal_handler(sig, frame):
    """Handle keyboard interruption and print statistics."""
    print_stats()
    sys.exit(0)


# Set up signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

# Process input line by line
for line in sys.stdin:
    try:
        parts = line.split()
        if len(parts) >= 7:
            file_size = int(parts[-1])
            status_code = parts[-2]
            total_file_size += file_size
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
            line_count += 1
            if line_count % 10 == 0:
                print_stats()
    except Exception:
        pass

# Print final statistics after processing all lines
print_stats()
