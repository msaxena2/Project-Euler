__author__ = 'manasvi'
from math import sqrt

def fact_count(num):
    count = 0
    for i in xrange(1, int(sqrt(num)) + 1):
        if num % i == 0:
            count += 1
        return count
start = 100
while(True):
    t_num = start*(start+1) / 2
    if fact_count(t_num) > 500:
        print t_num
        break
    start += 1