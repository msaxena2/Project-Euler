__author__ = 'manasvi'

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
