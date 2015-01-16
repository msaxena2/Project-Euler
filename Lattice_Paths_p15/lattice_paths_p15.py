__author__ = 'manasvi'
from math import factorial
def lattice_paths(n):
    return factorial(2 * n) / (factorial(n) * factorial(n))

#change n here
print(lattice_paths(20))
