__author__ = 'manasvi'
import math

"""
Problem Definition:

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

prime_counter = 1
num = 3
while(True):
    if is_prime(num):
        prime_counter += 1


    if prime_counter == 10001:
        print num
        break
    num += 2