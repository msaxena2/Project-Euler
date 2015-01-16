__author__ = 'manasvi'

def find_collatz_num(startnum):
    count = 1
    while(startnum != 1):
        while(startnum != 1):
            count += 1
            if startnum % 2 == 0:
                startnum = startnum /2
            else:
                startnum = startnum * 3 + 1
        return count

def find_max_collatz(max):
    max_count = 0
    collatz_num = -1
    for i in xrange(max, 1, -1):
        count = find_collatz_num(i)
        if count > max_count:
            max_count = count
            collatz_num = i
    print collatz_num

find_max_collatz(1000000)