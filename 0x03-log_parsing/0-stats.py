#!/usr/bin/python3
"""
file: 0-stats.py
"""


import sys
import signal

# Initialize variables
total_file_size = 0
status_code_count = {
                     200: 0, 301: 0, 400: 0, 401: 0,
                     403: 0, 404: 0, 405: 0, 500: 0
                    }
line_count = 0


def signal_handler(sig, frame):
    """a signal handler to catch CTRL+C
    """
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


def print_stats():
    """Helper function to print the statistics
    """
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_code_count.keys()):
        if status_code_count[status_code] > 0:
            print(f"{status_code}: {status_code_count[status_code]}")


for line in sys.stdin:
    try:
        fields = line.strip().split()
        if len(fields) == 7:
            if fields[3].isdigit() and fields[4].isdigit():
                status_code = int(fields[3])
                file_size = int(fields[4])
                if status_code in status_code_count:
                    status_code_count[status_code] += 1
                total_file_size += file_size
                line_count += 1
                if line_count == 10:
                    print_stats()
                    line_count = 0
    except KeyboardInterrupt:
        pass

print_stats()
