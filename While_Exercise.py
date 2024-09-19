# phrase = 'Python is a multi-paradigm programming language.' \
#      'Python was created by Guido van Rossum.'

phrase = input('Type a phrase: ')

i = 0
qty = 0
common_letter = ''

while i < len(phrase):
    current_letter = phrase[i]
    i += 1

    if current_letter == ' ':
        continue

    current_qty = phrase.count(current_letter)

    if qty < current_qty:
        qty = current_qty
        common_letter = current_letter

print(
    'The letter that appeared most often was',
f'"{common_letter}" which appeared {qty}x.')