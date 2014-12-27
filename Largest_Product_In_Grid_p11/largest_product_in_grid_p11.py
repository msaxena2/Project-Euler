__author__ = 'manasvi'
def parse_input(filename):
    file = open(filename)
    matrix = []
    for line in file:
        matrix.append(map(int, line.split()))
    return matrix


def find_max_product(matrix):
    

print parse_input("input.txt")[2][3]