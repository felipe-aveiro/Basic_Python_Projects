"""
Iterating strings with while
"""

#       01234567
name = 'Felipe Aveiro'
#      -12345678

name_size = len(name)

counter = 0

while counter < len(name):
    
    print(f'*{name[counter]}', end='')
    counter += 1
else:
    print('*')