"""
Write a program that asks the user to enter an integer,
and informs whether this number is even or odd. If the user does not enter an integer,
inform that it is not an integer.
"""

while True:
    i = input("Enter any number: ")

    if i == False:
        print('Type something!')
        continue

    try:
        i = int(i)

        if (i % 2) == 0:
            print('The number you have chosen is even!')

        else:
            print('The number you have chosen is odd!')
        break
    except:
        print('Choose a whole number!')
        continue

"""
Write a program that asks the user for the time and, based on the time specified,
displays the appropriate greeting. E.g.
Good morning (0-11), Good afternoon (12-17) and Good evening (18 - 23)
"""

while True:
    time = input("What time is it? ")

    if time == False:
        print('Type something!')
        continue

    if len(time) == 1:
        time = time + ":"

    try:
        x = time[0:2]

        if x[1] == ':' or x[1] == '-':
            x = x[0]
    
        if x.isdigit:
            x = int(x)
            if x >= 0 and x <= 11:
                print('Good morning!')
                break
            elif x >= 12 and x <= 17:
                print('Good afternoon!')
                break
            elif x >= 18 and x <= 23:
                print('Good evening!')
                break
            else:
                print('The hour digits can only range from 00 to 23!')
                continue

    except:
        print('The input must be a time in the format 00:00 or 00-00!')
        continue

"""
Write a program that asks for the user's first name.
If the name has 4 letters or less, write "Your name is short";
if it has between 5 and 6 letters, write "Your name is normal";
if it has more than 6 letters, write "Your name is too long"
"""

while True:
    name = input('Enter your first name: ')

    if name == '':
        print('Enter a name!')
        continue

    while True:
        letters = 0
        for a in range(len(name)):
            if name[a] == ' ':
                break
            a += 1
        break

    if a <= 4:
        print("Your name is short")
    elif a == 5 or a == 6:
        print("Your name is normal")
    elif a > 6:
        print("Your name is too long")

    break

