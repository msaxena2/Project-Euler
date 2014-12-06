__author__ = 'manasvi'

def sum_square_difference(n):
    return  pow((n * (n + 1)) / 2, 2) - (n * (n + 1) * ((2 * n) + 1) / 6)

#change n here
print sum_square_difference(100)