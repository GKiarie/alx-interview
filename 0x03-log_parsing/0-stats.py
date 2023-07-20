#!/usr/bin/python3
"""script that reads stdin line by
line and computes metrics
"""
import sys
import signal


def parse_line(line):
    """parse input line and extract status code and file size"""
    parts = line.split(" ")
    if len(parts) > 4:
        status_code = parts[-2]
        file_size = int(parts[-1])
        return status_code, file_size
    return None, None


def print_metrics(total_size, status_counts):
    """print computed metrics"""
    print(f"Total file size: {total_size}")
    for status_code, count in sorted(status_counts.items()):
        if count > 0:
            print(f"{status_code}: {count}")


def process_input():
    """process input lines and compute metrics"""
    status_codes_dict = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                         '404': 0, '405': 0, '500': 0}
    total_size = 0
    count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            status_code, file_size = parse_line(line)
            if status_code is not None and file_size is not None:
                status_codes_dict[status_code] += 1
                total_size += file_size
                count += 1

            if count == 10:
                count = 0  # reset count
                print_metrics(total_size, status_codes_dict)

        # Print final statistics
        print_metrics(total_size, status_codes_dict)

    except KeyboardInterrupt:
        # If interrupted, print final statistics before exiting
        print_metrics(total_size, status_codes_dict)
        sys.exit(0)


if __name__ == "__main__":
    import sys
    process_input()
