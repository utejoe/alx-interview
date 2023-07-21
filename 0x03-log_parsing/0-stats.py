#!/usr/bin/python3
import sys

def print_stats(total_size, status_codes):
    print("File size:", total_size)
    for status_code in sorted(status_codes):
        print("{}: {}".format(status_code, status_codes[status_code]))

if __name__ == "__main__":
    total_size = 0
    status_codes = {}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            data = line.split()
            if len(data) >= 9:
                status_code = data[-2]
                file_size = data[-1]
                try:
                    file_size = int(file_size)
                    status_code = int(status_code)
                except ValueError:
                    continue

                total_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1
                else:
                    status_codes[status_code] = 1

                if line_count % 10 == 0:
                    print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

