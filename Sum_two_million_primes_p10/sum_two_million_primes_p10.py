__author__ = 'manasvi'
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def find_sum(limit):
    arr = [1] * limit
    #Sieve of Eratosthenes
    sum = 0
    for i in xrange(2, limit+1):
        if arr[i-1] == 1:
            #number is prime
            sum += i
            for j in xrange(i, limit+1, i):
                arr[j-1] = -1
    return sum

#change n here
print find_sum(2000000)

