"""
Calculator with while
"""
result = None

while True:
    number_1 = input('Enter the first number: ')
    try:
        number_1 = float(number_1)
        while True:
            number_2 = input('Enter the second number: ')
            try:
                number_2 = float(number_2)
                while True:
                    operator = input('Enter the operator: ')
                    if operator == '+':
                        result = number_1 + number_2
                    elif operator == '-':
                        result = number_1 - number_2
                    elif operator == '*':
                        result = number_1 * number_2
                    elif operator == '/':
                        result = number_1 / number_2
                    elif operator == '**':
                        result = number_1 ** number_2
                    elif operator == '//':
                        result = number_1 // number_2
                    elif operator == '%':
                        result = number_1 % number_2
                    else:
                        print('Please enter a valid operator (+, -, *, /, **, //, %)')
                        continue
                    if result is not None:
                        break
            except ValueError:
                print('Enter a number!')
                continue
            
            if result is not None:
                break
            
    except ValueError:
        print('Enter a number!')
        continue

    if result is not None:
        break

print(f'The result of {number_1} {operator} {number_2} is {result}!')