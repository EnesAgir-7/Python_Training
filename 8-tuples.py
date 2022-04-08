three_numbers =(1,2,3)
number = (1,'Home', True,3,2)

#!  burada error verdi ( tuple doesn't support item assignment) bu liste ile tuple arasindali farktir
#!  three_numbers[1] = 23
print(three_numbers[0])
print(len(three_numbers))
print(type(three_numbers))

# listenin icerisindeki elemenlerin turune bakila bilinir #! bool mu string mi int oldugu
print(type(number[0]))

#^ ----------------------------------------------

kume = {"yellow", "blue", "green", "red", "black"}

for renk in kume:
    #! burada her seferinde baska bir siralama gelir bunun nedeni sets lerin sirassi onemli degildir
    print(renk)


