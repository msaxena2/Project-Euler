__author__ = 'manasvi'

def parse_input(input_file):
    file = open(input_file)
    matrix = []
    for line in file:
        matrix.append(map(int, line.split()))
    return matrix

def max_sum(matrix):
    max_path_arr = matrix[len(matrix) - 1]
    while(len(max_path_arr) != 1):
        current_arr = matrix[len(max_path_arr) - 2]
        temp_max_arr = []
        for i in xrange(0, len(current_arr)):
            temp_max_arr.append(max(current_arr[i] + max_path_arr[i], current_arr[i] + max_path_arr[i+1]))
        max_path_arr = temp_max_arr
    return max_path_arr

print("Sol to p18")
print(max_sum(parse_input("input.txt")))
print ("Sol to p67")
print(max_sum(parse_input("input2.txt")))
