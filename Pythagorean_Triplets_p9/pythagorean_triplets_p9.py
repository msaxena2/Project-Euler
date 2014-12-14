import math
"""

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def find_triplets():
    for i in xrange(1, 1000):
        for j in xrange(1, 1000):
            if (2000 * (i + j)) - (2 * i * j) == 1000000:
                return (math.sqrt((i * i) + (j * j)) * i * j)

print int(find_triplets())