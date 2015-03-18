__author__ = 'manasvi'

day_count = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def count_sunday_year(day, leap_status):

    sunday_count = 0
    for i in range(0, 12):
        if i != 2:
            day = (day + day_count[i]) % 7

        else:
            if leap_status == "leap":
                day = (day + 29) % 7
            else:
                day = (day + day_count[i]) % 7

        if (day == 1):
            sunday_count += 1

    return (sunday_count, day)

init_day = 3
total_count = 0
for i in range(1901, 1902):
    if (i % 100) != 0 and (i % 4) == 0:
        count, init_day = count_sunday_year(init_day, "leap")
    else:
        count, init_day = count, init_day = count_sunday_year(init_day, "unleap")
    total_count += count

print(total_count)
