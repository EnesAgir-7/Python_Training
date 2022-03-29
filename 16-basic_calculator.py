num1 = int(input('Enter first number: '))
op = input('Enter Operators')
num2 = int(input('Enter second number: '))


if op == '+':
    print('The addition is',num1+num2)
elif op == '-':
    print('The subtaction is',num1-num2)
elif op == '*':
    print('The multiplication is',num1*num2)
elif op == '/':
    print('The division is',abs(num1/num2))
else:
    print('Invalid operator')