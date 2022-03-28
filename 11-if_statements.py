value = int(input('Input a number: '))

if value%5 ==0:
    print(value,' can be divided by 5')
else:
    print(value,' can not be divided by 5')

#! -----------------------------------------
value = input('Input a value')

if type(value) == str:
    print(value+' is a string')
# elif type(value) == int:
#     print(value+' is a integer')
# elif type(value) == list:
#     print(value+' is a list')
else:
    print('WE don\'t know the data type of ', value)

#! -----------------------------------------
a= input('Enter first number: ')
b= input('Enter second number: ')

if a>b:
    print(str(a)+ ' greater than '+str(b))

elif(a<b):
    print(str(b)+' greater than '+str(a))

else:
    print(str(b)+' equal '+str(a))

#! -----------------------------------------
y= False

if y == True:
    print('Y is True')

elif y == False:
    print('Y is False')

else: #! x != True || x != False 
    print('Y is none of the two')

#! -----------------------------------------
boy = True
short = False

if boy == True and short == True:
    print('He is a short boy')
elif boy != True or short != True:
    print('He isn`t a short boy')