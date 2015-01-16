__author__ = 'manasvi'

#This works in python, donno how, but not the right sol, given even long is 64 bits and we need 1000.

print reduce(lambda x, y: x+y, map(int, (list(str(int(pow(2, 1000)))))))