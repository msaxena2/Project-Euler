__author__ = 'manasvi'
def parse_input(filename):
    file = open(filename)
    matrix = []
    for line in file:
        matrix.append(map(int, line.split()))
    return matrix


def find_max_product(matrix):
   max_product = -1
   for i in xrange(0, len(matrix)):
       for j in xrange(0, len(matrix[0])):
           if (j + 3) < len(matrix[0]):
               sub_max = matrix[i][j] * matrix[i][j+1] * matrix[i][j+2] * matrix[i][j+3]
               if sub_max > max_product:
                   max_product = sub_max
           if (i + 3) < len(matrix):
               sub_max = matrix[i][j] * matrix[i+1][j] * matrix[i+2][j] * matrix[i+3][j]
               if sub_max > max_product:
                   max_product = sub_max
           if (i + 3) < len(matrix) and (j + 3) < len(matrix[0]):
               sub_max = matrix[i][j] * matrix[i+1][j+1] * matrix[i+2][j+2] * matrix[i+3][j+3]
               if sub_max > max_product:
                   max_product = sub_max
           if (i + 3) < len(matrix) and (j - 3) >= 0:
               sub_max = matrix[i][j] * matrix[i+1][j-1] * matrix[i+2][j-2] * matrix[i+3][j-3]
               if sub_max > max_product:
                   max_product = sub_max
   print(max_product)


find_max_product(parse_input("input.txt"))
