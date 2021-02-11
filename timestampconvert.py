import datetime

timestamp = 1579117901
value = datetime.datetime.fromtimestamp(timestamp)
print(f"{value:%Y-%m-%d %H:%M:%S}")
