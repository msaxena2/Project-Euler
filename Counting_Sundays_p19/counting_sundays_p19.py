__author__ = 'manasvi'

"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""


day_count = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_dict = {0: "Sun", 1: "Mon", 2: "Tue", 3: "Wed", 4: "Thu", 5: "Fri", 6: "Sat"}


def count_sunday_year(day, leap_status):
    sunday_count = 0
    for i in range(0, 12):
        if (day == 0):
            sunday_count += 1
        if i != 1:
            day = (day + day_count[i]) % 7

        else:
            if leap_status == "leap":
                day = (day + 29) % 7
            else:
                day = (day + day_count[i]) % 7

    return (sunday_count, day)

init_day = 2
total_count = 0
for i in range(1901, 2001):
    if (i % 100) != 0 and (i % 4) == 0:
        count, init_day = count_sunday_year(init_day, "leap")
    else:
        count, init_day = count, init_day = count_sunday_year(init_day, "unleap")
    total_count += count

print(total_count)
