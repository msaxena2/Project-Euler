__author__ = 'manasvi'
"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

prev_num = 1
for i in xrange(100, 0, -1):
    prev_num = prev_num * i
    while(True):
        if(prev_num % 10 == 0):
            prev_num /= 10
        else:
            break

total_sum = 0
while(prev_num != 0):
    total_sum += prev_num % 10
    prev_num /= 10

print(total_sum)
