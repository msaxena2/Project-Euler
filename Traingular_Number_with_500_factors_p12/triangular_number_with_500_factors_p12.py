__author__ = 'manasvi'
from math import sqrt

prime_list = [2]

def is_prime(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def fact_count(num):
    #populate prime list
    for i in range(prime_list[-1], int(sqrt(num) + 1)):
        if is_prime(i):
            prime_list.append(i)

    prime_dict = {}

    while i < len(prime_list):



start = 100
while(True):
    t_num = (start*(start+1)) / 2
    fact = fact_count(t_num)
    if fact >= 500:
        print t_num
        break
    start += 1