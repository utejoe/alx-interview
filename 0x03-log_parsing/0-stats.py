#!/usr/bin/python3

import sys

def print_stats(total_size, status_codes):
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

def parse_line(line):
    parts = line.split(" ")
    if len(parts) < 7:
        return None, None
    ip = parts[0]
    status_code = parts[-2]
    file_size = int(parts[-1])
    return status_code, file_size

def main():
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    count = 0

    try:
        for line in sys.stdin:
            status_code, file_size = parse_line(line.strip())
            if status_code is not None and status_code.isdigit() and int(status_code) in status_codes:
                total_size += file_size
                status_codes[int(status_code)] += 1
                count += 1

                if count % 10 == 0:
                    print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        pass

    print_stats(total_size, status_codes)

if __name__ == "__main__":
    main()
