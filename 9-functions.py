#=> girdileri kullanicidan alip bir cikti olusturmak
def greetings_funsion3(name, age):
    print('Welcome '+name+'. You are '+str(age)+' years old.') 
    
name =input('Enter your name: ')
age = input('Enter your age: ')

greetings_funsion3(name,age)


#^ normal bir fonksiyon
def greetings_function():
    print('Welcome User')

greetings_function()


#* name is iceride verip print ini alirken bir cikti almak zorundayiz
def greetings_funsion1(name):
    print('Welcome '+name) 

greetings_funsion1('Enes')


#? int i string e cevirmek icin 
def greetings_funsion2(name):
    print('Welcome '+str(name)) 

greetings_funsion2(34)


#& funksiona 2 tana girdi vere biliriz (ad ve yas gibi)
def greetings_funsion3(name, age):
    print('Welcome '+name+'. You are '+str(age)+' years old.') 

greetings_funsion3('Pasha',34)
#& yukaridaki ile ayni sonuc cikar
def greetings_funsion4(name, age):
    print('Welcome '+name+'. You are '+str(age)+' years old.') 

greetings_funsion4(name='Tim',age=14)


#~  " * " isareti birden fazla girdinin oldugunu gosterir
def greetings_funsion5(*names):
    print('Welcome '+names[2]) 

greetings_funsion5('Enes','Pasha','Tim')

