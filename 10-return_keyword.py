def my_function():
    return 5+4

print(my_function())


def my_function(num1, num2):
    return num1+num2

print(my_function(7,5))


def add_numbers(num1, num2):
    print('Hello')
    return num1+num2

num1 = int(input('enter first number: '))
num2 = int(input('enter second number: '))
print(add_numbers(num1,num2))