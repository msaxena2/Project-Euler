__author__ = 'manasvi'



def max_13(digit_list):
    max_product = -1

    for i in range(0, len(digit_list)-12):
        local_prd = 1
        for j in range(i, i+13):
            local_prd *= digit_list[j]
        if local_prd > max_product:
            max_product = local_prd
    print(max_product)





file = open("input.txt")
digit_list = []
for line in file:
    for char in line:
        if char.isdigit():
            digit_list.append(int(char))

max_13(digit_list)