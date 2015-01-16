__author__ = 'manasvi'

"""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

P.S. input file for numbers

"""

def find_10_sum(matrix):
    index = len(matrix[0]) - 1
    carryover = 0
    digits = []
    while(index >= 0):
        sum = carryover
        for i in range(0, len(matrix)):
            sum += matrix[i][index]
        if index != 0:
            digits.append(sum % 10)
            carryover = sum / 10
        else:
            last = map(int, list(str(sum)))
            for num in reversed(last):
                digits.append(num)
        index -= 1
    final_str = ""
    for digit in reversed(digits[-10:]):
        final_str += str(digit)
    print final_str

def parse_input(filename):
    file = open(filename)
    matrix = []
    for line in file:
        matrix.append(map(int, list(line.rstrip())))
    return matrix

find_10_sum(parse_input("input.txt"))