__author__ = 'manasvi'


def find_sum(limit):
    arr = [1] * limit
    #Sieve of Eratosthenes
    sum = 0
    for i in xrange(2, limit+1):
        if arr[i-1] == 1:
            print i
            #number is prime
            sum += i
            for j in xrange(i, limit+1, i):
                arr[j-1] = -1
    return sum

print find_sum(2000000)

