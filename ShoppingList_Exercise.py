"""
Make a shopping list with lists
The user must be able to
insert, delete and list values from his list
Do not allow the program to crash with
errors of non-existent indexes in the list
"""
import os

list_ = []

while True:
    entry = input(f'\nSelect an option\n[i]nsert\t[d]elete\t[l]ist\t[f]inish: ')

    if entry.lower() == 'i':
        os.system('cls')
        while True:
            insert = input(f'\nItem: ')
            if insert == '' or insert.isdigit():
                os.system('cls')
                print(f'\nPlease enter a valid value for the shopping list!\n')
                continue
            elif insert.lower() == 'exit':
                break
            else:
                list_.append(insert)
                break

    elif entry.lower() == 'd':
        os.system('cls')
        while True:
            delete = input(f'\nSelect the index you want to delete: ')
            if delete.lower() == 'exit':
                break
            try:
                delete = int(delete)
                del list_[delete]
                break
            except ValueError:
                os.system('cls')
                print(f'\nPlease choose a valid index!')
                continue
            except IndexError:
                os.system('cls')
                print(f'\nChoose an index within the list range!')
                continue

    elif entry.lower() == 'l':
        os.system('cls')
        print(f'\n------------------------------')
        for item in enumerate(list_):
            ind, name = item
            print(ind, f'\t{name}')
        print('------------------------------')

    elif entry.lower() == 'f':
        os.system('cls')
        print(f'\nYou have completed your shopping list!')
        print(f'\n------------------------------')
        for item in enumerate(list_):
            ind, name = item
            print(ind, f'\t{name}')
        print('------------------------------')
        break

    else:
        os.system('cls')
        print(f'\nPlease select any option!')
        continue
