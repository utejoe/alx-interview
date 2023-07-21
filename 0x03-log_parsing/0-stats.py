#!/usr/bin/python3
#!/~/ute/alx-interview/0x03-log_parsing/python3.4.3


import sys
import re

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
            # Use regular expression to match the relevant fields in the log line
            match = re.match(r'(\d+\.\d+\.\d+\.\d+) - \[.*\] "GET \/projects\/260 HTTP\/1\.1" (\d+) (\d+)', line)
            if match:
                ip_address, status_code, file_size = match.groups()
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
    except PermissionError:
        sys.exit("Permission denied. Make sure the script has executable permission.")

