from glob import iglob
from os.path import join
from itertools  import zip_longest
from datetime import datetime
from columnar import columnar # pip install columnar
import argparse

PATH_HISTORY = '/home/gianmaria/Desktop/whodidwhat'
HISTORY_LEADING = '.bash_history_'


def print_history(user: str, from_date: str, to: str):
    history_list = []
    for history_file in iglob(f"{join(PATH_HISTORY, HISTORY_LEADING)}*"):
        user_history = history_file.split("/")[-1].replace(HISTORY_LEADING, "")
        with open(history_file, "r") as f:
            for date, cmd in zip_longest(*[f]*2):
                date = datetime.utcfromtimestamp(int(date.strip()[1:]))
                cmd = cmd.strip()
                history_list.append([date, user_history, cmd])
    
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
        table = columnar(history_list, headers=None, no_borders=True)
        print(table)    

def parse_date(date: str) -> datetime:
    return datetime.strptime(date, '%Y-%m-%d %H:%M')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='show who run the commands')
    parser.add_argument('-u', '--user', help='filter by user')
    parser.add_argument('--from', dest='from_date', help='filter only entries from a certain date (format YYYY-MM-DD HH:MM)')
    parser.add_argument('--to', help='filter only entries to a certain date (format YYYY-MM-DD HH:MM)')
    args = parser.parse_args()

    print_history(args.user, args.from_date, args.to)
