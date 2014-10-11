__author__ = 'Manasvi Saxena'
"""
Problem Statement:


If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Proposed soln. works in O(1) time.

"""


def find_sum(ceiling):
    for num in range(1, 4):
        if (ceiling - num) % 3 == 0:
            three_ceiling = ceiling - num
    for num in range(1, 6):
        if (ceiling - num) % 5 == 0:
            five_ceiling = ceiling - num
    for num in range(1, 16):
        if (ceiling - num) % 15 == 0:
            fifteen_ceiling = ceiling - num

    three_ap = ((three_ceiling / 3) * (3 + three_ceiling)) / 2
    five_ap = ((five_ceiling / 5) * (5 + five_ceiling)) / 2
    fifteen_ap = ((fifteen_ceiling / 15) * (15 + fifteen_ceiling)) / 2

    return (three_ap + five_ap) - fifteen_ap


def main():
    #change this value to change ceiling. Default is 1000.
    print find_sum(1000)

if __name__ == '__main__':
    main()
