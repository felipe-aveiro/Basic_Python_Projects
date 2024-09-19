import random

i = random.randint(0, 100) # random number will be set
tries = 0
list_ = []


def incorrect_guess(guess, list):
        print(f'{guess} is not the correct number!')
        list.append(guess)
        list.sort()
        print(f'List of numbers already tried: {list}\n')

while (True):
    entry = input("From 0 to 100, what was the number drawn? ")
    tries = tries + 1

    try:
        entry = int(entry)
        if (entry == i):
            print(f'\nCongratulations, you got it right after {tries} attempts! The drawn number was {i}!\n')
            break

        if (entry > i):
            print(f'\nThe drawn number is less than {entry}!')
            incorrect_guess(entry, list_)
            continue

        if (entry < i):
            print(f'\nThe drawn number is greater than {entry}!')
            incorrect_guess(entry, list_)
            continue

    except ValueError:
        print("Only integer entries from 0 to 100 are allowed!")
        continue
