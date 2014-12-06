__author__ = 'manasvi'

def twenty_multiple(num_list):
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    factor_list = []
    while(True):
        for prime in primes:
           while(True):
               div_count = 0
               for index in range(0, len(num_list)):
                   number = num_list[index]
                   if(number != 1 and (number % prime) == 0):
                       if div_count == 0:
                           factor_list.append(prime)
                       div_count = div_count + 1
                       num_list[index] = number / prime
               if div_count == 0:
                   break
        all_one = True
        for num in num_list:
            all_one and (num == 1)
        if all_one:
            break
    final_ans = 1
    for num in factor_list:
        final_ans *= num
    return final_ans

def main():
    numlist = []
    for i in range(1, 21):
        numlist.append(i)
    print twenty_multiple(numlist)

if __name__ == '__main__':
    main()
