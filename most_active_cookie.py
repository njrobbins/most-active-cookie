from datetime import datetime
import csv
import os
import sys


def example():
    print(f"\nExample: python3 {sys.argv[0]} file.csv -d {current_date}")


def check_arg_length(args):
    if len(args) == 4:
        return True


def check_if_csv(csv_file):
    if os.path.splitext(csv_file)[-1].lower() == ".csv":
        return True


def check_flag(flag):
    if flag == "-d":
        return True


def check_datetime_format(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        print("Date must be in format: yyyy-mm-dd")


def is_file_empty(csv_file):
    csv_file_length = [row for row in csv.DictReader(csv_file)]
    if len(csv_file_length) == 0:
        print("CSV file is empty.")
        return True


def has_header(csv_file):
    # 2048 is arbitrary; it's big enough to read the first 2-3 rows
    csv_reader = csv_file.read(2048)
    # Rewind
    csv_file.seek(0)
    return csv.Sniffer().has_header(csv_reader)


def count_cookies():
    for row in cookie_log.readlines():
        cookie, timestamp = row.split(",")
        timestamp = timestamp.replace("\n", "")
        # Convert timestamp into datetime object
        timestamp_datetime = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S%z")
        if datetime_arg.strftime("%Y-%m-%d") == timestamp_datetime.strftime("%Y-%m-%d"):
            if cookie in cookie_occurrences:
                cookie_occurrences[cookie] += 1
            else:
                cookie_occurrences[cookie] = 1


current_date = datetime.today().strftime("%Y-%m-%d")
cookie_occurrences = {}

if not check_arg_length(sys.argv):
    print(f"Must have following arguments: {sys.argv[0]} <csv_file> -d yyyy-mm-dd")
    example()
    exit(1)

if not check_if_csv(sys.argv[1]):
    print("File type must be CSV.")
    example()
    exit(1)

if not check_flag(sys.argv[2]):
    print('Command line flag must be "-d".')
    example()
    exit(1)

if not check_datetime_format(sys.argv[3]):
    example()
    exit(1)

# Open cookie log CSV file in read mode
cookie_log = open(sys.argv[1], "r")

# Convert given datetime argument into datetime object
datetime_arg = datetime.strptime(sys.argv[3], "%Y-%m-%d")

if is_file_empty(cookie_log):
    exit(1)
else:
    cookie_log.seek(0)

if has_header(cookie_log):
    # Skip header
    next(cookie_log)
    count_cookies()
else:
    count_cookies()

if len(cookie_occurrences) != 0:
    max_occurred = max(cookie_occurrences.values(), key=lambda x: x)
else:
    print("Date not found.")
    exit(1)

for cookie, occurrences in cookie_occurrences.items():
    if occurrences == max_occurred:
        print(cookie)

cookie_log.close()
