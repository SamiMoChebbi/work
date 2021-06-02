from glob import iglob
from os.path import join
from itertools  import zip_longest
from datetime import datetime
from columnar import columnar # pip install columnar

PATH_HISTORY = '/home/gianmaria/Desktop/whodidwhat'
HISTORY_LEADING = '.bash_history_'

def get_history(path_history, history_file_leading):
    history_list = []
    for history_file in iglob(f"{join(path_history, history_file_leading)}*"):
        user = history_file.split("/")[-1].replace(history_file_leading, "")
        with open(history_file, "r") as f:
            for date, cmd in zip_longest(*[f]*2):
                date = datetime.utcfromtimestamp(int(date.strip()[1:]))
                cmd = cmd.strip()
                history_list.append([date, user, cmd])
    return sorted(history_list)


if __name__ == "__main__":
    # TODO: add filters, like filter by user, or select date range
    # --user gdelmont
    # --from YY-MM-DD HH:MM  --to YY-MM-DD HH:MM
    history = get_history(PATH_HISTORY, HISTORY_LEADING)
    if history:    
        table = columnar(history, headers=None, no_borders=True)
        print(table)
