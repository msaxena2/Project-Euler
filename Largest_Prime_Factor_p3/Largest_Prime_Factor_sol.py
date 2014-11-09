from math import sqrt

__author__ = 'manasvi'
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

Approach is very naive. To be improved
"""

def check_prime(num):
    print "checking prime"
    for i in xrange(3, num/2):
        if num % i == 0:
            return False
    return True


def largest_pf(num):
    print "here came"
    for i in xrange(int(sqrt(num))+1, 2, -1):
        if(num % i == 0):
            if check_prime(i):
                return i
    return num


def main():
    #change this value to change ceiling. Default is 1000.
    print largest_pf(600851475143)

if __name__ == '__main__':
    main()
