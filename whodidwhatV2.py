#!/usr/bin/python3

from glob import iglob
from os.path import join
from itertools  import zip_longest
from datetime import datetime
from tabulate import tabulate
import argparse
import re
from os import environ
from tzlocal import get_localzone # pip install tzlocal

PATH_HISTORY = '/root'
HISTORY_LEADING = '.bash_history_'

local_tz = get_localzone()

def print_history(user: str, from_date: str, to: str):
    history_list = []
    for history_file in iglob(f"{join(PATH_HISTORY, HISTORY_LEADING)}*"):
        user_history = history_file.split("/")[-1].replace(HISTORY_LEADING, "")
        with open(history_file, "r") as f:
            date = convert_unix_time(0)
            for line in f.readlines():
                line = line.strip()
                if re.match("#[0-9]+", line):
                    # this is a datestamp in unix format, convert into datetime
                    date = convert_unix_time(int(line[1:]))
                else:
                    # line is a command
                    history_list.append([date, user_history, line])

    # filter data
    if user:
        history_list = filter(lambda h: h[1] == user, history_list)
    if from_date:
        from_date = parse_date(from_date)
        history_list = filter(lambda h: h[0] >= from_date, history_list)
    if to:
        to_date = parse_date(to)
        history_list = filter(lambda h: h[0] <= to_date, history_list)

    history_list = sorted(history_list)
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
    parser.add_argument('--from', dest='from_date', help='filter only entries from a certain date (format YYYY-MM-DD HH:MM)')
    parser.add_argument('--to', help='filter only entries to a certain date (format YYYY-MM-DD HH:MM)')
    args = parser.parse_args()

    print_history(args.user, args.from_date, args.to)
