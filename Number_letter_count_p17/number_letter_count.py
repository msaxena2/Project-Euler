__author__ = 'manasvi'
"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
"""

def get_word(n):
    ones = {0 : "",
            1 : "one",
            2 : "two",
            3 : "three",
            4 : "four",
            5 : "five",
            6 : "six",
            7 : "seven",
            8 : "eight",
            9 : "nine"}

    doubles  = {10 : "ten",
                11 : "eleven",
                12 : "twelve",
                13 : "thirteen",
                14 : "fourteen",
                15 : "fifteen",
                16 : "sixteen",
                17 : "seventeen",
                18 : "eighteen",
                19 : "nineteen",
                20 : "twenty",
                30 : "thirty",
                40 : "forty",
                50 : "fifty",
                60 : "sixty",
                70 : "seventy",
                80 : "eighty",
                90 : "ninety",}

    hundreds = {0 : "",
            1 : "one hundred",
            2 : "two hundred",
            3 : "three hundred",
            4 : "four hundred",
            5 : "five hundred",
            6 : "six hundred",
            7 : "seven hundred",
            8 : "eight hundred",
            9 : "nine hundred"}

    thousands = {1 : "one thousand"}

    word_store = {0 : ones,
                  1 : doubles,
                  2 : hundreds,
                  3 : thousands}

    nstring = str(n)
    word = ""
    for i in range(len(nstring) - 1, -1, -1):
        if i > 1:
            word += word_store[i][int(nstring[len(nstring) - i - 1])]
        else:
            if len(nstring) > 2 and nstring[-2:] == "00":
                    return word
            if len(nstring) > 2 and nstring[-2:] != "00":
                word += " and"

            if len(nstring) >= 2:
                if nstring[-2:] == "00":
                    return word

                if nstring[-2] == "0" and len(word) > 0:
                    word += " " + word_store[0][int(nstring[-1])]
                    return word

                if nstring[-2] == "0" and len(word) == 0:
                    word += word_store[0][int(nstring[-1])]
                    return word

                if nstring[-2] == "1" and len(word) > 0:
                    word += " " + word_store[1][int(nstring[-2:])]
                    return word
                if nstring[-2] == "1" and len(word) == 0:
                    word += word_store[1][int(nstring[-2:])]
                    return word
                if len(word) > 0:
                    word += " " + word_store[1][int(nstring[-2]+"0")] + " " + word_store[0][int(nstring[-1])]
                else:
                    word += word_store[1][int(nstring[-2]+"0")] + " " + word_store[0][int(nstring[-1])]

                return word

            else:
                return word_store[0][int(nstring[-1])]

letter_count = 0
for i in range(1, 1001):
    word = get_word(i)
    word = ''.join(word.split())
    letter_count += len(word)
print letter_count