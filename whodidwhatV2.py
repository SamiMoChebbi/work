#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import re
from datetime import datetime
from glob import iglob
from os.path import join

from tabulate import tabulate
from tzlocal import get_localzone

# Constants
PATH_HISTORY = '/root'
HISTORY_LEADING = '.bash_history_'
DATE_PATTERN = re.compile("#[0-9]+")

# Get local timezone once
local_tz = get_localzone()

def print_history(user: str, from_date: datetime, to: datetime):
    history_list = []

    for history_file in iglob(f"{join(PATH_HISTORY, HISTORY_LEADING)}*"):
        user_history = history_file.split("/")[-1].replace(HISTORY_LEADING, "")
        if user and user_history != user:
            continue

        with open(history_file, "r") as f:
            date = convert_unix_time(0)
            for line_number, line in enumerate(f, 1):  # start line_number from 1
                try:
                    line = line.strip()
                    if DATE_PATTERN.match(line):
                        date = convert_unix_time(int(line[1:]))
                        if from_date and date < from_date:
                            break
                        if to and date > to:
                            continue
                    else:
                        history_list.append([date, user_history, line])
                except Exception as e:
                    print(f"Error in file {history_file} on line {line_number}: {line}")
                    print(f"Exception: {e}")
                    return

    history_list.sort()
    if history_list:
        table = tabulate(history_list, headers=None, tablefmt="plain")
        print(table)

def convert_unix_time(t: int) -> datetime:
    return datetime.fromtimestamp(t).astimezone(local_tz)

def parse_date(date: str) -> datetime:
    return datetime.strptime(date, '%Y-%m-%d %H:%M')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='show who run the commands')
    parser.add_argument('-u', '--user', help='filter by user')
    parser.add_argument('--from', dest='from_date', help='filter only entries from a certain date (format YYYY-MM-DD HH:MM)', type=parse_date)
    parser.add_argument('--to', help='filter only entries to a certain date (format YYYY-MM-DD HH:MM)', type=parse_date)
    args = parser.parse_args()

    print_history(args.user, args.from_date, args.to)
