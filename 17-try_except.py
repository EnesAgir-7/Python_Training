try:
    x = int(input('Input an integer: '))
    print(x)
except ValueError:
    print('Value not an integer')
else:
    print('nothing went wrong')

#! ---------------------------------------
try:
    x = int(input('Input an integer: '))
    print(x)
except ValueError:
    print('Value not an integer')
finally:
    print('try except finished')