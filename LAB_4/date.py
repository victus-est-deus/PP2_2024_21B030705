import datetime


# 1
def subtract_five_days():
    t = datetime.datetime.now()
    fdb = t - datetime.timedelta(days=5)
    return fdb


print(subtract_five_days())


# 2
def print_relative_days():
    t = datetime.date.today()
    y = t - datetime.timedelta(days=1)
    tmrw = t + datetime.timedelta(days=1)
    print(f"Yesterday: {y}")
    print(f"Today: {t}")
    print(f"Tomorrow: {tmrw}")


print_relative_days()


# 3
def drop_microseconds():
    current_time = datetime.datetime.now()
    time_without_microseconds = current_time.replace(microsecond=0)
    return time_without_microseconds


print(drop_microseconds())


# 4
def date_difference_in_seconds(d1, d2):
    difference = d2 - d1
    return difference.total_seconds()


d1 = datetime.datetime(2024, 6, 20, 15, 30)
d2 = datetime.datetime(2024, 6, 25, 15, 30)
print(date_difference_in_seconds(d1, d2))
