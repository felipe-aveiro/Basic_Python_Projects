i = input("How big will the pyramid be? ")
try:
    i = int(i)
    if i < 0:
            print("Input must be a positive integer!")
    else:
        for x in range(i + 1):
            for a in range((i + 1) - x):
                print(' ', end="")
            for b in range(x):
                print('#', end="")
            print()
except:
    print('You must enter an integer!')
