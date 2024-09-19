"""
CPF: 746.824.890-70 (brazilian taxpayer ID number).

Collect the sum of the first 9 digits of the CPF
multiplying each of the values by a
countdown starting from 10

Ex.: 746.824.890-70 (746824890)
    10  9  8  7  6  5  4  3  2
*   7   4  6  8  2  4  8  9  0 
    70  36 48 56 12 20 32 27 0

Add all the results:
70+36+48+56+12+20+32+27+0 = 301
Multiply the previous result by 10
301 * 10 = 3010
Get the remainder by the division of the previous result by 11:
3010 % 11 = 7
If the previous result is greater than 9:
    the result is 0
the opposite of this:
    the result is the amount of the account

The first digit of the CPF is 7

    11 10  9  8  7  6  5  4  3  2
*   7   4  6  8  2  4  8  9  0  7 <-- FIRST DIGIT
    77  40 54 64 14 24 40 36 0 14

Add all the results:
77+40+54+64+14+24+40+36+0+14 = 363
363 * 10 = 3630
Get the remainder by dividing the previous result by 11:
3630 % 11 = 0
If the previous result is greater than 9:
    the result is 0
the opposite of this:
    the result is the value of the account
"""
import random
import sys
import re


while True:
    random_cpf = ''

    for i in range(9):
        random_cpf += str(random.randint(0,9))

    if random_cpf[0]*len(random_cpf) == random_cpf:
            print('CPFs with repeated numbers are not valid! Generating another CPF...')
            continue
        
    sum_ = 0
    i = 10

    for dig in random_cpf:
            dig = int(dig)
            sum_ += (i * dig)
            i -= 1
    
    digit_1 = (sum_ * 10) % 11

    digit_1 = digit_1 if digit_1 <= 9 else 0

    sum_ = 0
    i = 11

    for dig in (random_cpf + str(digit_1)):
        dig = int(dig)
        sum_ += (i * dig)
        i -= 1
    
    digit_2 = (sum_ * 10) % 11

    digit_2 = digit_2 if digit_2 <= 9 else 0

    random_cpf = (random_cpf[:3] + '.' + random_cpf[3:6] + '.' + random_cpf[6:] + '-' + str(digit_1) + str(digit_2))

    print(f'The randomly generated CPF is {random_cpf}!')
    break

while True:

    user_cpf = input('Enter your CPF: ')

    cpf_num = re.sub(
        r'[^0-9]', # catches everything that is not a number
        '',         # replaces with an empty space
        user_cpf)

    if cpf_num[0]*len(cpf_num) == cpf_num:
        print('CPFs with repeated numbers are not valid!')
        continue

    try:
        if user_cpf.isdigit():
            user_cpf = (user_cpf[:3] + '.' + user_cpf[3:6] + '.' + user_cpf[6:9] + '-' + user_cpf[9:])
            sum_ = 0
            i = 10

            for dig in user_cpf[:12]:
                if dig.isdigit():
                    dig = int(dig)
                    sum_ += (i * dig)
                    i -= 1
                else:
                    continue

            digit_1 = (sum_ * 10) % 11

            digit_1 = digit_1 if digit_1 <= 9 else 0

            sum_ = 0
            i = 11

            for dig in (user_cpf[:12] + str(digit_1)):
                if dig.isdigit():
                    dig = int(dig)
                    sum_ += (i * dig)
                    i -= 1
                else:
                    continue

            digit_2 = (sum_ * 10) % 11

            digit_2 = digit_2 if digit_2 <= 9 else 0

            generated_cpf = user_cpf[:12] + str(digit_1) + str(digit_2)

            if user_cpf == generated_cpf:
                print(f'{user_cpf} is valid!')
                break
            else:
                print('Invalid CPF!')
                continue

        elif (user_cpf[:3] + user_cpf[4:7] + user_cpf[8:11] + user_cpf[12:]).isdigit():
            sum_ = 0
            i = 10

            for dig in user_cpf[:12]:
                if dig.isdigit():
                    dig = int(dig)
                    sum_ += (i * dig)
                    i -= 1
                else:
                    continue

            digit_1 = (sum_ * 10) % 11

            digit_1 = digit_1 if digit_1 <= 9 else 0

            sum_ = 0
            i = 11

            for dig in (user_cpf[:12] + str(digit_1)):
                if dig.isdigit():
                    dig = int(dig)
                    sum_ += (i * dig)
                    i -= 1
                else:
                    continue

            digit_2 = (sum_ * 10) % 11

            digit_2 = digit_2 if digit_2 <= 9 else 0

            generated_cpf = user_cpf[:12] + str(digit_1) + str(digit_2)

            if user_cpf == generated_cpf:
                print(f'{user_cpf} is valid!')
                break
            else:
                print('Invalid CPF!')
                continue
        else:
            print('Enter a valid CPF!')
            continue

    except ValueError:
        print('Enter a valid CPF!')
        continue