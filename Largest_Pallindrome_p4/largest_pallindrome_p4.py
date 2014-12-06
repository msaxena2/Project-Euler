__author__ = 'manasvi'


def is_palindrome(num):
    rev = 0
    temp_num = num
    while(temp_num > 0):
        rev = (rev * 10) + ((temp_num) % 10)
        temp_num = temp_num / 10
    return rev == num



def find_palindrome():
    max_palindrome = 0
    for i in xrange(1000, 0, -1):
        for j in xrange(1000, 0, -1):
            if is_palindrome(i * j) and (i * j) > max_palindrome:
                max_palindrome = (i * j)
    return max_palindrome

def main():
    p = find_palindrome()
    if(p > 0):
        print p
    else:
        print "none"

if __name__ == '__main__':
    main()
